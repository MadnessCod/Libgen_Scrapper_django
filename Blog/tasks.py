import os
import time

import requests
import wget
from celery import shared_task
from bs4 import BeautifulSoup

from django.conf import settings
from django.utils import timezone
from .models import Author, Publisher, Year, Language, Extension, Book
from .resources import BookResource


def scrapper_again(phrase, export_format):
    try:
        counter = 1
        while True:
            data_scraped = list()
            url = f'https://libgen.is/search.php?req=/{phrase.replace(" ", "+")}&page={counter}'
            text = requests.get(url, timeout=10)
            if text.status_code == requests.codes.ok:
                content = BeautifulSoup(text.text, 'html.parser')
                tr = content.find('table', class_='c').find_all('tr')
                if len(tr) > 1:
                    main_path = os.path.join(
                        settings.MEDIA_ROOT,
                        f'{phrase}_{timezone.now().date()}'
                    )
                    if not os.path.exists(main_path):
                        os.makedirs(main_path, exist_ok=True)

                    for i in range(1, len(tr)):
                        for m, j in enumerate(tr[i].find_all('td')):
                            if m == 1:
                                author = ','.join([element.text for element in j.find_all('a')])
                                data_scraped.append(author)
                                continue

                            if m == 2:
                                title = [element.text for element in j.find('a').contents][0]
                                data_scraped.append(title)
                                continue
                            if m == 9:
                                temp_url = j.find('a').get('href')
                                file_downloader.delay(temp_url, main_path)
                                continue
                            data_scraped.append(j.text)

                        author_instance, _ = Author.objects.get_or_create(
                            title=data_scraped[1],
                        )
                        publisher_instance, _ = Publisher.objects.get_or_create(
                            title=data_scraped[3],
                        )
                        year_instance, _ = Year.objects.get_or_create(
                            title=data_scraped[4],
                        )
                        language_instance, _ = Language.objects.get_or_create(
                            title=data_scraped[6].lower(),
                        )
                        extension_instance, _ = Extension.objects.get_or_create(
                            title=data_scraped[8],
                        )
                        if not Book.objects.filter(title=data_scraped[2]):
                            Book.objects.create(
                                author=author_instance,
                                publisher=publisher_instance,
                                year=year_instance,
                                language=language_instance,
                                type=extension_instance,
                                size=data_scraped[7],
                                number=data_scraped[0],
                                title=data_scraped[2],
                                page=data_scraped[9],
                                is_download=True,
                            )
                        data_scraped.clear()

                    dataset = BookResource().export(Book.objects.filter(is_download=True))

                    if export_format == 'csv':
                        export_path = os.path.join(
                            settings.MEDIA_ROOT, main_path, f'exported_data.{export_format}'
                        )
                        with open(export_path, 'w') as f:
                            f.write(dataset.csv)
                    elif export_format == 'xls':
                        export_path = os.path.join(
                            settings.MEDIA_ROOT, main_path, f'exported_data.{export_format}'
                        )
                        with open(export_path, 'wb') as f:
                            f.write(dataset.xls)
                    elif export_format == 'json':
                        export_path = os.path.join(
                            settings.MEDIA_ROOT, main_path, f'exported_data.{export_format}'
                        )
                        with open(export_path, 'w') as f:
                            f.write(dataset.json)

                    Book.objects.filter(is_download=True).update(is_download=False)

                else:
                    if counter == 1:
                        return 'no result'
                    else:
                        return data_scraped
            else:
                return 'Connection error'
            counter += 1

    except requests.exceptions.RequestException as error:
        print(f'Request error {error}')
    except AttributeError as error:
        print(f'Attribute Error {error}')
    except EOFError as error:
        print(f'EOF Error {error}')
    except OSError as error:
        print(f'OS Error {error}')


@shared_task
def file_downloader(link, base_dir):
    """this function downloads files of the book to base_dir directory"""
    for attempt in range(settings.MAX_RETRIES):
        try:
            s = requests.Session()
            text = s.get(link, timeout=10).text
            link_file = BeautifulSoup(text, 'html.parser').find('h2').find('a').get('href')
            image = BeautifulSoup(text, 'html.parser').find('img').get('src')
            image_url = f'https://libgen.is/{image}'
            wget.download(
                url=image_url,
                out=base_dir,
                bar=wget.bar_adaptive
            )
            wget.download(
                url=link_file,
                out=base_dir,
                bar=wget.bar_adaptive
            )
            break
        except requests.exceptions.ConnectionError as error:
            print(f'Connection Error {error}')
        except requests.exceptions.RequestException as error:
            print(f'Request Error {error}')
        except AttributeError as error:
            print(f'Attribute Error {error}')
        except OSError as error:
            print(f'OS error {error}')
            if attempt < settings.MAX_RETRIES:
                print(f'Retrying in {settings.RETRY_DELAY}')
                time.sleep(settings.RETRY_DELAY)
            else:
                print(f"couldn't download {link}")

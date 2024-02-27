import os
import requests
import wget
from django.utils import timezone
from bs4 import BeautifulSoup

data_scrape_dict = {}
filename_tuple = tuple()


def main(phrase):
    global data_scrape_dict
    try:
        counter = 1
        while True:
            url = f'https://libgen.is/search.php?req=/{phrase.replace(" ", "+")}&page={counter}'
            text = requests.get(url, timeout=10)
            if text.status_code == requests.codes.ok:
                content = BeautifulSoup(text.text, 'html.parser')
                tr = content.find('table', class_='c').find_all('tr')
                if len(tr) > 1:
                    main_path = os.getcwd() + f'\\media\\{phrase}_{timezone.now().date()}'
                    if not os.path.exists(main_path):
                        os.makedirs(main_path, exist_ok=True)

                    scrapper(tr, main_path, counter)
                else:
                    if counter == 1:
                        return 'no result'
                    else:
                        return data_scrape_dict
            else:
                return 'Connection Error'
            counter += 1
    except requests.exceptions.ConnectionError as error:
        print(f'Connection Error {error}')
    except AttributeError as error:
        print(f'Attribute Error {error}')
    except EOFError as error:
        print(f'EOFError {error}')
    except OSError as error:
        print(f'OSError {error}')


def scrapper(soup, temp_dir, number):
    global data_scrape_dict
    data_scrape = []
    try:
        for i in range(1, len(soup)):
            for m, j in enumerate(soup[i].find_all('td')):
                if m == 1:
                    data_scrape.append(','.join([element.text for element in j.find_all('a')]))
                    continue
                if m == 2:
                    title = [element.text for element in j.find('a').contents][0]
                    data_scrape.append(title)
                    link = j.find('a').get('href')
                    temp_url = f'https://libgen.is/{link}'
                    image_downloader(temp_url, temp_dir)
                    continue
                if m == 9:
                    temp_url = j.find('a').get('href')
                    file_downloader(temp_url, temp_dir)
                data_scrape.append(j.text)
            data_scrape = data_scrape[:9]
            data_scrape.append(temp_dir)
            data_scrape_dict[f'data{number}{i}'] = data_scrape.copy()
            data_scrape.clear()
    except AttributeError as error:
        print(f'AttributeError {error}')
    except ValueError as error:
        print(f'Value error: {error}')
    except TypeError as error:
        print(f'Type error {error}')


def image_downloader(link, base_dir):
    global filename_tuple
    try:
        text = requests.get(link, timeout=10).text
        soup = BeautifulSoup(text, 'html.parser')
        tr = soup.find('table').find_all('tr')
        for i, j in enumerate(tr):
            if i == 1:
                image_url = f"https://libgen.is/{j.find('a').find('img').get('src')}"

                filename = wget.download(
                    url=image_url,
                    out=base_dir,
                    bar=wget.bar_adaptive
                )
                filename_tuple += (filename,)
    except requests.exceptions.ConnectionError as error:
        print('error', error)
    except AttributeError as error:
        print(f'Attribute Error {error}')


def file_downloader(link, base_dir):
    global filename_tuple
    try:
        text = requests.get(link, timeout=10).text
        link_file = BeautifulSoup(text, 'html.parser').find('h2').find('a').get('href')

        file_name = wget.download(url=link_file,
                                  out=base_dir,
                                  bar=wget.bar_adaptive
                                  )
        filename_tuple += (file_name,)
    except requests.exceptions.ConnectionError as error:
        print(f'Connection Error {error}')

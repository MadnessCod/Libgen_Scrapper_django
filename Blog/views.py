import os
import shutil
from django.shortcuts import render, HttpResponse
from .forms import UserInputForm
from .models import ScrapperData
from .scraper import main
from import_export.formats import base_formats
from .resources import ScrapedDataResource


def scrape_and_display(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phrase = form.cleaned_data['phrase']
            export_format = form.cleaned_data['export_format']
            scrape_data = main(phrase)
            if isinstance(scrape_data, dict):
                export_dir = scrape_data['data11'][9]
                for key, value in scrape_data.items():
                    if key.startswith('data'):
                        if not ScrapperData.objects.filter(number=value[0]).exists():
                            ScrapperData.objects.create(
                                number=value[0],
                                author=value[1],
                                title=value[2],
                                publisher=value[3],
                                year=value[4],
                                page=value[5],
                                language=value[6],
                                size=value[7],
                                type=value[8],
                                path=value[9],
                            )

                scrapper_data_resource = ScrapedDataResource()
                dataset = scrapper_data_resource.export()

                if export_format == 'csv':
                    export_path = os.path.join(export_dir, 'exported_data.csv')
                    exported_data = base_formats.CSV().export_data(dataset)
                    with open(export_path, 'w', encoding='utf-8') as f:
                        f.write(exported_data)
                elif export_format == 'xls':
                    export_path = os.path.join(export_dir, 'exported_data.xls')
                    exported_data = base_formats.XLS().export_data(dataset)
                    with open(export_path, 'wb') as f:
                        f.write(exported_data)
                elif export_format == 'json':
                    export_path = os.path.join(export_dir, 'exported_data.json')
                    exported_data = base_formats.JSON().export_data(dataset)
                    with open(export_path, 'w') as f:
                        f.write(exported_data)
                shutil.make_archive(f'{export_dir}_', 'zip', export_dir)
                return HttpResponse(f'The data is ready location is : {export_dir}_.zip')
            elif scrape_data == 'no result':
                return HttpResponse('no result for your search')
            elif scrape_data == 'Connection error':
                return HttpResponse('Connection Error')
            else:
                return HttpResponse('Unexpected error happened')
        else:
            form = UserInputForm()
            return render(request, 'enter_phrase.html', {'form': form})
    else:
        form = UserInputForm()
        return render(request, 'enter_phrase.html', {'form': form})

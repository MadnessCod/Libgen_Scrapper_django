from django.shortcuts import render, HttpResponse

from .forms import UserInputForm
from .tasks import scrapper_again


def scrape_and_display(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phrase = form.cleaned_data['phrase']
            export_format = form.cleaned_data['export_format']
            scrape_data = scrapper_again(phrase, export_format)
            if isinstance(scrape_data, list):
                return HttpResponse('success')
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

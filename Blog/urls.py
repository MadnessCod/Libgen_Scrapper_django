from django.urls import path
from .views import scrape_and_display


urlpatterns = [
    path('scrape-and-display/', scrape_and_display, name='scrape_and_display'),
]

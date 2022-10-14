from django.urls import path
from scraping.views import bt_scraping

urlpatterns = [
    path('bt', bt_scraping, name='bt-scraping'),
]

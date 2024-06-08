from django.urls import path
from . import views

urlpatterns = [
    path('taskmanager/start_scraping/', views.CoinMarketCapView.as_view()),
    path('taskmanager/scraping_status/<str:job_id>/', views.CoinMarketCapView.as_view()),
]
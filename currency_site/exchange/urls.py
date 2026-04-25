from django.urls import path
from . import views

urlpatterns = [
    path("", views.rate_list, name="rate_list"),
    path("save-today/", views.save_today_rates, name="save_today_rates"),
    path("today/", views.today_rates, name="today_rates"),
    path("api/today/", views.today_rates_api, name="today_rates_api"),
]
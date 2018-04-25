from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.hotelList, name="index"),
    path("ajax/hotel/", views.hotelJson, name='hotelJson'),
]



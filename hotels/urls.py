from django.urls import path
from . import views
from . import helper

app_name = "news"

urlpatterns = [
    path("", views.hotelList, name="index"),
    path("ajax/hotel/", views.hotelJson, name='hotelJson'),
]

helper.setListOfHotels()

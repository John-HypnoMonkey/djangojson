from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, Hotel
from django.forms.models import model_to_dict
from django.utils.text import Truncator
from . import helper
# Create your views here.


def hotelList(request):
    #country_list = Country.objects.order_by("-name")
    country_list = helper.ListOfHotels.keys()
    context = {
             'country_list': country_list
              }
    return render(request, "hotels/list.html", context)


def hotelJson(request):
    #country_id = request.GET.get('country_id', None)
    #hotels_models_list = Hotel.objects.filter(country__id__exact=country_id).order_by('name')
    #hotels = list(hotels_models_list.values('name', 'price', 'image'))
    #for item in hotels:
    #    item['truncated_name'] = Truncator(item['name']).chars(15)
    country = request.GET.get('country_id', None)
    sorting = request.GET.get('sorting', None)
    if country in helper.ListOfHotels:
        if sorting == '1':
            hotels = helper.ListOfHotelsPriceToUp[country]
        elif sorting == '2':
            hotels = helper.ListOfHotelsPriceToDown[country]
        else:
            hotels = helper.ListOfHotels[country]
    else:
        hotels = ()
    data = {
            'hotels': hotels
    }
    return JsonResponse(data)

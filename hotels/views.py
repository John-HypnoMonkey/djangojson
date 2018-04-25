from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, Hotel
from django.forms.models import model_to_dict
from django.utils.text import Truncator
# Create your views here.


def hotelList(request):
    country_list = Country.objects.order_by("-name")
    context = {
             'country_list': country_list
              }
    return render(request, "hotels/list.html", context)


def hotelJson(request):
    country_id = request.GET.get('country_id', None)
    hotels_models_list = Hotel.objects.filter(country__id__exact=country_id).order_by('name')
    hotels = list(hotels_models_list.values('name', 'price', 'image'))
    for item in hotels:
        item['truncated_name'] = Truncator(item['name']).chars(15)
    data = {
            'hotels': hotels
    }
    return JsonResponse(data)

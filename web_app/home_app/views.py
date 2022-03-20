from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from web_scrapping.web_scrapping import HeliumWeb, HeliumHotspot


def index(request):
    network = HeliumWeb()
    hotspot = HeliumHotspot()

    return HttpResponse(f'Hotspot is {hotspot.get_status()}. \n'
                        f'Percentage of offline rak is {network.get_percentage_of_offline_hotspots()}')


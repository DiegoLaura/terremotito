from random import randrange

from django.http.response import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def get_chart(_request):
    serie = []
    counter = 0

    while counter < 7:
        serie.append(randrange(100, 400))
        counter += 1

    chart = {
        "xAxis": [
            {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat ", "Sun"]
            }
        ],
        "yAxis": [
            {
                "type": "value"
            }
        ],
        "series": [
            {
                "data": serie,
                "type": "line"
            }
        ],
    }

    return JsonResponse(chart)


def sismo(request):
    return render(request, "sismo.html")

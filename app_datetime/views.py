from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def datetime_view(request):
    if request.method == "GET":
        data = datetime.now()  # Написать, что будет возвращаться из данного представления
        return HttpResponse(f"Текущее время {data}.")# Вернуть объект HttpResponse с необходимыми данными

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def customers(request):
    return HttpResponse("<h1>Xayrullayev Abdurahmon Hotamjon o'gli</h1>"
                        "<h1>Tojidininov Rustam Alisher o'gli</h1>")


def data(request):
    return HttpResponse("<h1>Hello about biography for customerspage</h1>")

from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello this is library homepage</h1>")

def about(request):
    return render(request, "h1.html")
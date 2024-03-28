from django.urls import path
from .views import customers, data

urlpatterns = [
    path('customers/', customers, name='customers'),
    path('data/', data, name='data'),
]

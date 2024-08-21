from . import views
from django.urls import path
from .views import currencies
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('', csrf_exempt(currencies.as_view()), name='preferences') #when {% url preferences%}, then  this is called on 
]
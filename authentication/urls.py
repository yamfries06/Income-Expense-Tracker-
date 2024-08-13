from .views import RegistrationView
from django.urls import path 

urlpatterns = [ 
    path('register', RegistrationView.as_view(), name="register") #called on the class to create an instance of the view that can handle the request.
]
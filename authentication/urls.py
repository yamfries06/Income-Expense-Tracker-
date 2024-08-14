from .views import RegistrationView, UsernameValidationView, EmailValidationView
from django.urls import path 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [ 
    path('register', RegistrationView.as_view(), name="register"), #called on the class to create an instance of the view that can handle the request.
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate_email")
]
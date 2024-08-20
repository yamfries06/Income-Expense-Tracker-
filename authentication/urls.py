from .views import RegistrationView, UsernameValidationView, EmailValidationView, loginView
from django.urls import path 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [ 
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate_email"),
    path('register', csrf_exempt(RegistrationView.as_view()), name="register"), #called on the class to create an instance of the view that can handle the request.
    path('login', csrf_exempt(loginView.as_view()), name="login")
]
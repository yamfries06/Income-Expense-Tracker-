from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.

class RegistrationView(View):
    def get(self, request): 
        return render(request, 'authentication/register.html')
    
    def post(self, request): 
        #GET USE DATA
        #VALIDATE
        #CREATE USER ACCOUNT
        username = request.POST.get('username')
        email = request.POST.get('email') 
        password = request.POST.get('password')
    
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists(): 
                if len(password) < 6:
                    messages.error(request, 'password too short')
                    return render(request, 'authentication/register.html')
        
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)

                user.save() 
                messages.success(request, 'Account succesfully created') #stored in hte session so it can be displayed in the next HTTP Response when render the website again
                return render(request, 'base.html')
            
        return render(request, 'authentication/register.html')
    
class loginView(View): 
    def get(self, request): 
        return render(request, 'authentication/login.html')
    
    def post(self, request): 
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password: 
            user=auth.authenticate(username=username, password=password)
            if user: 
                auth.login(request, user)
                messages.success(request, 'Welcome, '+user.username+'. You are now logged in')
                return redirect('expenses')
            else: 
                messages.error(request, 'Invalid Credentials, try again')
            return render(request, 'authentication/login.html')

class UsernameValidationView(View): 
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['username']
            
            # Check if the username is alphanumeric
            if not str(username).isalnum():
                return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'username_error': 'Sorry, this username is in use - please choose another'}, status=409)
            
            # If the username is valid
            return JsonResponse({'username_valid': True})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class EmailValidationView(View): 
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            
            if not validate_email(email):
                return JsonResponse({'email_error': 'email invalid'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'email_error': 'Sorry, this email is already registered'}, status=409)
            
            # If the username is valid
            return JsonResponse({'email_valid': True})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class LogoutView(View):
    def post(self, request): 
        auth.logout(request)
        messages.success(request, "You have been logged out")
        return redirect('mainpage')

def mainpage(request): 
    return render(request, 'base.html')

        

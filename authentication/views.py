from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 

# Create your views here.

class RegistrationView(View):
    def get(self, request): 
        return render(request, 'authentication/register.html')
    
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
from django.shortcuts import render, redirect
import os 
import json 
from django.conf import settings
from django.views import View
from .models import UserPreference
from django.contrib import messages



class currencies(View): #inheriting View, which gives the class the ability to process HTTP requests 
    def get(self, request): 
        return self.render(request)
        
    def post(self, request): 
        if request.user.is_authenticated: 
            user_preferences, created = UserPreference.objects.get_or_create(user=request.user)
            currency=request.POST['currency']
            user_preferences.currency=currency
            user_preferences.save() 
            messages.success(request, 'Changes saved')
        else: 
            messages.error(request, 'You must log in first')
        return self.render(request) 
    
    def render(self, request):  #this would run first when page is loaded
        currency_data = [] 
        file_path=os.path.join(settings.BASE_DIR, 'currencies.json')
        with open(file_path, 'r') as file: 
            data=json.load(file) #loads json into python dictionary
            for k, v in data.items(): 
                currency_data.append({'name': k, 'value': v})
        if request.user.is_authenticated:
            try:
                user_preferences = UserPreference.objects.get(user=request.user)
                user_currency = user_preferences.currency
            except UserPreference.DoesNotExist:
                user_currency = 'USD'  # Set a default currency if no preferences exist
        else:
            user_currency = 'USD'  # Default if not authenticated

        # Pass currency data and user preferences to the template
        context = { 
            'currencies': currency_data,
            'currentCurrency': user_currency  # Use the user's preferred currency
        }
        
        return render(request, 'preferences/index.html', context)
    
    

        


    
    
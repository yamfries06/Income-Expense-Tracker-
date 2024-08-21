from django.shortcuts import render
import os 
import json 
from django.conf import settings
from django.views import View
from .models import UserPreference
from django.contrib import messages



class currencies(View): #inheriting View, which gives the class the ability to process HTTP requests 
    def get(self, request): 
        print("baba")
        currency_data = [] 
        file_path=os.path.join(settings.BASE_DIR, 'currencies.json')
        with open(file_path, 'r') as file: 
            data=json.load(file) #loads json into python dictionary
            for k, v in data.items(): 
                currency_data.append({'name': k, 'value': v})
        return render(request, 'preferences/index.html', {'currencies': currency_data})
    
    def post(self, request): 
        print("pepe")
        user_preferences=UserPreference.objects.get(user=request.user) 
        if user_preferences: 
            currency=request.POST['currency']
            user_preferences.currency=currency
            user_preferences.save() 
            messages.success(request, 'Changes saved')
        else: 
            messages.error(request, 'must login to save currency preference')
        return render(request, 'preferences/index.html', {'currencies': currency_data})

        


    
    
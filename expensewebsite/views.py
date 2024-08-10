from django.shortcuts import render 

def index(request): 
    print("rendering index view")
    return render(request, "index.html")
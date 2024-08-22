from django.shortcuts import render
from .models import Category, Expense
from django.contrib import messages 

def index(request): 
    categories = Category.objects.all() 
    return render(request, 'expenses/index.html')

def add_expense(request):
    categories = Category.objects.all() 
    context={
        'categories': categories
    }
    if request.method=='GET': 
        return render(request, 'expenses/add_expenses.html', context) 

    if request.method=='POST': 
        amount=request.POST['amount']
        if not amount:
            messages.error(request, "Amount not specified")
        return render(request, 'expenses/add_expenses.html', context)
        

        



from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib import messages 

def index(request): 
    expenses = Expense.objects.filter(owner=request.user)

    context = {
        'expenses': expenses
    }
    return render(request, 'expenses/index.html', context)

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


        description=request.POST['description']
        if not description: 
            messages.error(request, "description not specified")  
            return render(request, 'expenses/add_expenses.html', context)

        
        date=request.POST['date']
        category=request.POST['category']
        Expense.objects.create(amount=amount, date=date, category=category, description=description, owner=request.user )
        messages.success(request, 'Expenses saved succesfully')
        return redirect('expenses') 
    



        



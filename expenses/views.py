from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib import messages 
from userpreferences.models import UserPreference
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def index(request): 
    if not request.user.is_authenticated: 
        messages.error(request, "must login first")
        return render(request, 'expenses/index.html')
    else:  
        expenses = Expense.objects.filter(owner=request.user)
        try:
            user_preference = UserPreference.objects.get(user=request.user)
            currency = user_preference.currency if user_preference.currency else 'CAD'  # Fallback to default if blank
        except UserPreference.DoesNotExist:
            currency = 'CAD'  # Fallback default currency

        context = {
            'expenses': expenses,
            'currency': currency,
        }
        print("Context:", context)

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
        Expense.objects.create(amount=amount, date=date, category=category, description=description, owner=request.user)
        messages.success(request, 'Expenses saved succesfully')
        return redirect('expenses') 
    
def edit_expense(request, id): 

    expense=Expense.objects.get(pk=id) #finding the expense object with primary key = id
    
    if request.method == 'GET': 
        allCategories=Category.objects.all() 
        context = {
            'expense': expense,
            'values': expense,
            'categories': allCategories
        }
        return render(request, 'expenses/edit_expenses.html', context)
    
    elif request.method == 'POST': 
        expense.amount=request.POST['amount']
        expense.date=request.POST['date']
        expense.category=request.POST['category']
        expense.description=request.POST['description']
        expense.save()

        expenses = Expense.objects.all() 
        context = {
            'expenses': expenses,
        }
        messages.success(request, 'Handled Request')
        return render(request, 'expenses/index.html', context)


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'expense deleted')
    return redirect ('expenses')  #redirects to url with name 'expenses' 


def generate_summary(request): 
    expenses = Expense.objects.filter(owner=request.user)
    categoryTotal = {} 
    for expense in expenses: 
        categoryTotal[expense.category] = categoryTotal.get(expense.category, 0) + expense.amount
    
    labels = categoryTotal.keys() 
    sizes = categoryTotal.values() 
    colors = ["brown", "hotpink", "blue", "#4CAF50"]

    # Create the pie chart
    plt.figure(figsize=(6, 6))  # Define the figure size
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')  # Equal aspect ratio ensures the pie is a circle

    # Convert plot to PNG image and encode to base64
    buffer = io.BytesIO()  # Create an in-memory buffer
    plt.savefig(buffer, format='png')  # Save the plot as PNG to the buffer
    buffer.seek(0)  # Move the pointer to the start of the stream

    # Encode image to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()  # Close the buffer
    
    # Pass the base64 image to the template
    return render(request, 'expenses/summary.html', {'image_base64': image_base64})




    
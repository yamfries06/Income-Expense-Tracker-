from django.urls import path 
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expenses/', views.add_expense, name="add-expenses"),
    path('edit-expenses/<int:id>/', views.edit_expense, name="edit-expense"),
    path('delete-expense/<int:id>/', views.delete_expense, name="delete-expense"),
    path('summary/', csrf_exempt(views.generate_summary.as_view()), name='expense_summary'),

]
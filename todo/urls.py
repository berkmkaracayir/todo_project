# todo/urls.py
from django.urls import path
from .views import todo_list, add_todo, edit_todo, delete_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('edit/<int:todo_id>/', edit_todo, name='edit_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]
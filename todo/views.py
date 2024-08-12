# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')

def edit_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.delete()
    return redirect('todo_list')
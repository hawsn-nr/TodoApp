from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/list.html", {
        "todos": todos,
        "todos_count": todos.count(),
    })

def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title = title)
        return redirect("todo_list")

def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        new_title = request.POST.get('new_title')
        if new_title:
            todo.title = new_title
            todo.save()
    return redirect("todo_list")

def delete_todo(request, id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
    return redirect("todo_list")

def toggle_done(reqeust, id):
    todo = get_object_or_404(Todo, id=id)
    todo.done = not todo.done
    todo.save()
    return redirect("todo_list")
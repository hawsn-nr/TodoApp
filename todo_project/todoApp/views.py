from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect("todo_list")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todo_list")
    else:
        form = SignupForm()
    return render(request, "todo/signup.html", {"form": form})
@login_required
def todo_list(request):
    todos = Todo.objects.filter(owner=request.user)
    return render(request, "todo/list.html", {
        "todos": todos,
        "todos_count": todos.count(),
    })
    
@login_required
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title = title)
        return redirect("todo_list")

@login_required
def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        new_title = request.POST.get('new_title')
        if new_title:
            todo.title = new_title
            todo.save()
    return redirect("todo_list")

@login_required
def delete_todo(request, id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
    return redirect("todo_list")

@login_required
def toggle_done(reqeust, id):
    todo = get_object_or_404(Todo, id=id)
    todo.done = not todo.done
    todo.save()
    return redirect("todo_list")
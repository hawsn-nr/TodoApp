from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.todo_list, name='todo_list'),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="todo/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("create/", views.create_todo, name="create_todo"),
    path("update/<int:id>/", views.update_todo, name="update_todo"),
    path("delete/<int:id>/", views.delete_todo, name="delete_todo"),
    path("toggle/<int:id>/", views.toggle_done, name="toggle_done"),
    path("api/", include("todoApp.api_urls")),
]
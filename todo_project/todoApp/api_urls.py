from django.urls import path
from . import api_views

urlpatterns = [
    path("todos/", api_views.TodoListCreateAPIView.as_view(), name='api_todo_list'),
    path("todos/<int:pk>/", api_views.TodoRetrieveUpdateDestroyAPIView.as_view(), name='api_todo_detail'),
    path("todos/<int:pk>/toggle", api_views.TodoToggleDoneAPIview.as_view(), name="api_todo_toggle"),
    path("signup/", api_views.RegisterAPIView.as_view(), name='api_register'),
    path("login/", api_views.LoginAPIView.as_view(), name='api_login')
]
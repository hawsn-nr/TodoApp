from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Todo
from .serializers import TodoSerializer, RegisterSerializer

class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
class TodoToggleDoneAPIview(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
    def patch(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.done = not todo.done
        todo.save()
        
        serializer = self.get_serializer(todo)
        return Response(serializer.data)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request},)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key
        })
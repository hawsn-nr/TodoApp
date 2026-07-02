from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos", default=1)
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title
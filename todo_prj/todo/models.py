from django.db import models


# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

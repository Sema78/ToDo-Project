from rest_framework import serializers
from todo.models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'date_pub', 'completed']
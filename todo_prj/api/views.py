from rest_framework import generics
from .serializers import ToDoItemSerializer
from todo.models import ToDoItem


# Create your views here.
class ToDoItemList(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
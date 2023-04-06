from django.urls import path
from .views import ToDoItemList, ToDoItemDetail

urlpatterns = [
    path('todo/', ToDoItemList.as_view()),
    path('todo/<int:pk>/', ToDoItemDetail.as_view()),
]
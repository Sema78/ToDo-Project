from django.shortcuts import render, redirect

from .forms import ToDoItemForm
from .models import ToDoItem

# Create your views here.
def todo_list(request):
    todos = ToDoItem.objects.all()
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoItemForm()
    context = {'todos': todos, 'form': form}
    if 'completed_id' in request.POST:
        completed_todo = ToDoItem.objects.get(pk=request.POST['completed_id'])
        completed_todo.completed = True
        completed_todo.save()
    return render(request, 'todos/todo_list.html', context)
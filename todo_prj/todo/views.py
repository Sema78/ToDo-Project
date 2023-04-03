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
    if request.method == 'POST' and 'delete_id' in request.POST:
        todo_id =int(request.POST.get('delete_id'))
        todo = ToDoItem.objects.get(id=todo_id)
        todo.delete()
        return redirect('todo_list')
    if 'completed_id' in request.POST:
        completed_todo = ToDoItem.objects.get(pk=request.POST['completed_id'])
        completed_todo.completed = True
        completed_todo.save()
    return render(request, 'todo/todo_list.html', context)

from django.shortcuts import render, redirect

from todos.forms import TodoForm
from todos.models import Todo


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by("is_complete")
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request, 'todo_list.html', {'todos': todos, 'form': form})


def todo_complete(request, pk):
    todo = Todo.objects.get(id=pk)
    # todo.is_complete = not todo.is_complete
    todo.is_complete = True
    todo.save()
    return redirect('todo_list')


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_list')

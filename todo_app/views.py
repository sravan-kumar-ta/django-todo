from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    obj = Task.objects.all()
    return render(request, 'index.html', {'objects': obj})


def delete(request):
    if request.method == 'GET':
        obj_id = request.GET['obj_id']
        # print('sravan', obj_id)
        task = get_object_or_404(Task, id=obj_id)
        task.delete()
        return redirect('/')


def complete(request, id):
    task = get_object_or_404(Task, id=id)
    if task.is_complete == True:
        task.is_complete = False
        task.save()
    else:
        task.is_complete = True
        task.save()
    return redirect('/')


def test(request):
    return redirect(request, 'sample.html')

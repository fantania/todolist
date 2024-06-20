from django.shortcuts import render, get_object_or_404, redirect

from task.models import Task

# Create your views here.

def edit_task(request, pk):
    task = get_object_or_404(Task, pk= pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.name = new_task
        task.save()
        return redirect('home')

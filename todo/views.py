from django.shortcuts import render, redirect

from .models import Task

# Create your views here.
# http://127.0.0.1:8000/
def home(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'home.html', {'tasks' : tasks})

# http://127.0.0.1:8000/add/
def add_task(request):
    title = request.POST.get('title')
    Task.objects.create(title=title)
    return redirect('home')

# http://127.0.0.1:8000/delete/8
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

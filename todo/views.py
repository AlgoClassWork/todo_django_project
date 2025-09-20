from django.shortcuts import render

from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'home.html', {'tasks' : tasks})



from django.shortcuts import render

from .models import Task

# Create your views here.
# http://127.0.0.1:8000/
def home(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'home.html', {'tasks' : tasks})

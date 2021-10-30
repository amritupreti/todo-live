from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def index(request):
    return render(request, "index.html")

def task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        task = Task(title=title, description=description)
        task.save()
        return redirect("/")
    
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "task.html", context)

def updateTask(request, pk):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        task = Task.objects.get(pk=pk)

        task.title = title
        task.description = description
        
        task.save()
        return redirect("/")
    task = Task.objects.get(pk=pk)
    context = {
        "task": task
    }
    return render(request, "update.html", context)

def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('/')

def completeTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.task_status = not task.task_status 
    task.save()
    return redirect('/')
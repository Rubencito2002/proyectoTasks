from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

"""
def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
"""
class TaskViews(View):
    tasks = Task.objects.all()
    nombre_template = 'tasks/task_list.html'

    def actualizarTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self,request):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, self.nombre_template, {'tasks': self.actualizarTask(), 'form': form})

    def post(self,request):
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save()
            title = form.cleaned_data['tittle']
            description = form.cleaned_data['description']
            completed = form.cleaned_data['completed']
            Task.objects.create(title = title, description = description, completed = completed)
            return redirect('TaskViews')
        tasks = Task.objects.all()
        return render(request, self.nombre_template, {'tasks': self.actualizarTask(), 'form': form})
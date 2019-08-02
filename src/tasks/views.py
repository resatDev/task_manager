from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from projects.models import Project
from .models import Task
from .form import TaskForm

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Successfully Created!")
        return HttpResponseRedirect("/projects/"+ str(instance.pid)+"/tasks/"+str(instance.id))
    context = {
        "form": form,
    }
    return render(request, "add_task.html", context)

def task_details(request,pid=None,id=None):
    queryset = get_object_or_404(Task, id=id)
    project = get_object_or_404(Project, id = pid)
    context = {
        "task": queryset,
        "project": project
    }
    return render(request, "task_detail.html", context)
def task_list(request):
    queryset = Task.objects.all()
    project_list = Project.objects.all()
    context = {
        "task_list": queryset,
        "project_list":project_list
    }
    return render(request, "tasks_list.html", context)
def task_update(request, id=None):
    instance = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Successfully Saved!")
        return HttpResponseRedirect("/projects/"+ str(instance.pid)+"/tasks/"+str(instance.id))
        
    context = {
        "title":instance.title,
        "instance":instance,
        "form": form,
    }
    
    return render(request, "update_task.html", context)
def task_delete(request, id=None, pid=None):
    instance = get_object_or_404(Task, id=id)
    pid = instance.pid
    instance.delete()
    #messages.success(request, "Successfully Deleted!")
    #return HttpResponseRedirect("/projects/" + str(pid))
    return HttpResponseRedirect("/tasks/")

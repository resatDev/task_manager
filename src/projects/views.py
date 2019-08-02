from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Project
from tasks.models import Task
from .form import ProjectForm

@login_required(login_url="/")
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/projects/"+str(instance.id))
    context = {
        "form": form,
    }
    return render(request, "add_project.html", context)
@login_required(login_url="/")
def project_details(request,id=None):
    queryset = get_object_or_404(Project, id=id)
    task_list = Task.objects.filter(pid = id)
    context = {
        "project_list": queryset,
        "task_list": task_list
    }
    return render(request, "project_detail.html", context)

@login_required(login_url="/")
def project_list(request):
    queryset = Project.objects.all()
    context = {
        "project_list": queryset
    }
    return render(request, "projects.html", context)

@login_required(login_url="/")  
def project_update(request, id=None):
    instance = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Successfully Saved!")
        return HttpResponseRedirect("/projects/"+ str(instance.id))
        
    context = {
        "title":instance.title,
        "instance":instance,
        "form": form,
    }
    
    return render(request, "update_project.html", context)
#def project_delete(request):
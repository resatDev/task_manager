from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .form import UserLoginForm
from django.shortcuts import redirect
from projects.views import project_list

def login_view(request):
    print(request.user.is_authenticated)
    next=request.GET.get("next")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)
        print(request.user.is_authenticated)
        if next:
            return redirect(next)
        return redirect("/posts/")
    return render(request,"login.html",{"form":form})

#def register_view(request):

def logout_view(request):
    logout(request)
    print(request.user.is_authenticated)
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)
        print(request.user.is_authenticated)
        return redirect("/posts/")
    return render(request,"login.html",{"form":form})
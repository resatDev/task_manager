"""taskM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from . import views as projectViews
from tasks import views as taskViews
urlpatterns = [
    path('', projectViews.project_list),
    path('<int:id>/', projectViews.project_details),
    path('create/', projectViews.project_create),
    path('<int:pid>/tasks/<int:id>', taskViews.task_details),
    path('<int:id>/edit', projectViews.project_update),
    path('<int:pid>/tasks/<int:id>/delete/', taskViews.task_delete),
]
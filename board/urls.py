"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "board"
urlpatterns = [
    path('', views.index, name = "index"),
    path('detail/<bpk>', views.detail, name = "detail"),
    path('del/<bpk>', views.delete, name = "del"),
    path('create', views.create, name = "create"),
    path('create_reply/<bpk>', views.create_reply, name = "create_reply"),
    path('reply_del/<rpk>/<bpk>', views.reply_del, name = "reply_del"),
    path('addup/<bpk>', views.addup, name = "addup"),
    path('removeup/<bpk>', views.removeup, name = "removeup"),
]

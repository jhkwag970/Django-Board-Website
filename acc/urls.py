from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "acc"
urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.userlogin, name = "userlogin"),
    path('signup', views.signup, name = "signup"),
    path('logout', views.userlogout, name = "userlogout"),
    path('profile', views.profile, name = "profile"),
    path('userdel', views.userdel, name = "userdel"),
    path('usermod', views.usermod, name = "usermod"),
    path('follow/<wri>/<bpk>', views.follow, name = "follow"),
    path('unfollow/<wri>/<bpk>', views.unfollow, name = "unfollow"),
]
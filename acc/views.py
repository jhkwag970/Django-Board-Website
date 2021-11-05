from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User

def signup(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        nn = request.POST.get("nickname")
        co = request.POST.get("comment")
        pi = request.FILES.get("pic")
        User.objects.create_user(username=un, password=pw, nickname=nn, comment=co, pic=pi)
        return redirect("acc:index")
    return render(request, "acc/signup.html")

    
# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userlogin(request):
    un = request.POST.get("username")
    pw = request.POST.get("password")
    user = authenticate(username=un, password=pw)
    if user:
        login(request, user)
        messages.success(request, 'LOGIN SUCCESS')
    else:
        messages.error(request, 'LOGIN FAIL')
    return redirect('acc:index')

def userlogout(request):
    logout(request)
    return redirect('acc:index')

def profile(request):
    return render(request, 'acc/profile.html')

def userdel(request):
    u = User.objects.get(username = request.user.username)
    u.delete()
    return redirect("acc:index")

def usermod(request):
    if (request.method == "POST"):
        un = request.user.username
        u = User.objects.get(username = un)
        pw = request.POST.get("password")
        co = request.POST.get("comment")
        ni = request.POST.get("nickname")
        pi = request.FILES.get("pic")
        if pw:
            u.set_password(pw)
        if pi :
            u.pic = pi
        u.nickname = ni
        u.comment = co
        u.save()
        user = authenticate(username = un, pasword = pw)
        login(request, user)
        return redirect('acc:profile')
    return render(request, "acc/usermod.html")


def follow(request, wri, bpk):
    #follow 할 사람의 정보 가져오기
    u = User.objects.get(username = wri)
    #현재 로그인 되어 있는 사람의 follow (DB table) 에 u 정보 등록
    request.user.follow.add(u)
    return redirect('board:detail', bpk=bpk)

def unfollow(request, wri, bpk):
    #follow 할 사람의 정보 가져오기
    u = User.objects.get(username = wri)
    #현재 로그인 되어 있는 사람의 follow (DB table) 에 u 정보 등록
    request.user.follow.remove(u)
    return redirect('board:detail', bpk=bpk)
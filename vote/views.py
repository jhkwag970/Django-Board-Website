from django.shortcuts import render, redirect
from .models import Topic, choice
from acc.models import User
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    page = request.GET.get("page", 1)

    t = Topic.objects.all().order_by("-ctime")
    pag = Paginator(t, 4)
    obj = pag.get_page(page)
    
    context = {
        "topics" : obj,
    }
    return render(request, "vote/index.html", context)

def detail(request, tpk):
    t = Topic.objects.get(id = tpk)
    u = User.objects.get(username = t.writer)
    c = t.choice_set.all()
    context = {
        "topic" : t,
        "choices" : c,
        "pic" : u.getpic(),
    }
    return render(request, "vote/detail.html", context)

def vote(request, tpk):
    t = Topic.objects.get(id = tpk)
    if (not request.user in t.voter.all()):
        t.voter.add(request.user)
        c = request.POST.get("choice")
        ch = choice.objects.get(id =c)
        ch.voter.add(request.user)
    return redirect('vote:detail', tpk =tpk)

def cancel(request, tpk):
    t = Topic.objects.get(id = tpk)
    t.voter.remove(request.user)
    #역참조 해서 Topic과 연결된 모든 choice들을 가져옴
    c = t.choice_set.all()
    #Topic과 연결된 (Foreign key) 모든 choices들 반복문
    for i in c:
        #현재 로그인 되어 있는 유저가 Topic 과 연결된 Choice들의 각각 choicer(누가 이 choice에 투표했는지)를 탐색
        if request.user in i.voter.all():
            i.voter.remove(request.user)
    return redirect('vote:detail', tpk=tpk)

def create(request):
    if request.method == "POST":
        top = request.POST.get("topic")
        wri = request.user.username
        con = request.POST.get("content")
        t = Topic(subject=top, writer=wri, ctime=timezone.now(), content=con)
        t.save()
        sels = request.POST.getlist("select")
        coms = request.POST.getlist("comment")
        pics = request.FILES.getlist("pic")
        for i,j,k in zip(sels, coms, pics):
            choice(sub=t, select=i, comment=j, pic=k).save()
        return redirect("vote:index")

    return render(request, "vote/create.html")


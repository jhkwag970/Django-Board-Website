from django.shortcuts import redirect, render
from .models import Board, Reply
from acc.models import User
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    
    page = request.GET.get('page',1)
    cate = request.GET.get("cate")
    kw = request.GET.get("kw")

    if (cate == "sub"):
        b = Board.objects.filter(subject__contains = kw).order_by('-pubdate')
    elif (cate == "wri"):
        b = Board.objects.filter(writer = kw).order_by('-pubdate')
    elif (cate == "con"):
        b = Board.objects.filter(content__contains = kw).order_by('-pubdate')   
    else: 
        b = Board.objects.all().order_by('-pubdate')

    b = b.order_by('-pubdate')
    pag = Paginator(b, 10)
    obj = pag.get_page(page)

    context = {
        #"blist" : b 모든 게시글을 보여줌
        "blist" : obj, # paginator 로 한페이지에 10개씩만 보여줌
        "cate" : cate,
        "kw" : kw,
    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    #record들의 리스트 
    #record들은 reocord 와 비교해야함.
    b = Board.objects.get(id = bpk)
    r = b.reply_set.all()
    u = User.objects.get(username = b.writer)


    context = {
        "bo" : b,
        "pic" : u.getpic(),
        "rep" : r,
        "bwriter" : u,
    }
    return render(request, "board/detail.html", context)

def delete(request, bpk):
    b = Board.objects.get(id = bpk)
    # detail.html 에서 계정 주인이 아닐시 글 수적과 삭제를 막음
    # 하지만, url을 통해 접근하면, 삭제가 가능함
    # 그 경우를 막기 위해 삭제시 계정 이름을 확인함
    if b.writer == request.user.username:
        b.delete()
    else:
        return render(request, "error/forbidden.html")
    return redirect('board:index')

def create(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        wri = request.user.username
        con = request.POST.get("content")
        Board(subject=sub, writer=wri, content=con, pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(request, "board/create.html")

def create_reply(request, bpk):
    b = Board.objects.get(id = bpk)
    rep = request.user.username
    com = request.POST.get("comment")
    if com:
        Reply(sub=b, replyer=rep, comment = com).save()
    return redirect("board:detail", bpk = bpk)

def reply_del(request, rpk, bpk):
    r = Reply.objects.get(id = rpk)
    if (request.user.username == r.replyer):
        r.delete()
    return redirect("board:detail", bpk = bpk)

def addup(request, bpk):
    b = Board.objects.get(id = bpk)
    b.up.add(request.user)
    return redirect("board:detail", bpk = bpk)

def removeup(request, bpk):
    b = Board.objects.get(id = bpk)
    b.up.remove(request.user)
    return redirect("board:detail", bpk = bpk)
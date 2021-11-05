from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    pubdate = models.DateTimeField()
    # Board 와 User 의 N:N 관계 설정
    # User는 각기 다른 게시판의 좋아요를 누름
    # 각각의 Board의 게시판(record들)은 각기 다른 User들의 좋아요를 받음 
    up = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.subject
    
    def summary(self):
        if len(self.content) > 20:
            return self.content[:20] + "..."
        return self.content

class Reply(models.Model):
    sub = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.replyer

    def rep_pic(self):
        u = User.objects.get(username = self.replyer)
        return u.getpic()
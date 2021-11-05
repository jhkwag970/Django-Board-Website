from django.db import models
from django.db.models.deletion import CASCADE
from acc.models import User
from datetime import datetime 

# Create your models here.
class Book(models.Model):
    #각 유저마다의 북마크 페이지 생성
    user = models.ForeignKey(User, on_delete=CASCADE)
    site_name = models.CharField(max_length=100)
    site_url = models.TextField(default = 0)
    impo = models.BooleanField(default = False)
    ctime = models.DateTimeField(default=datetime.now())

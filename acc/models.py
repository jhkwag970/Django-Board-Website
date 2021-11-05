from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings
# Create your models here.
class User(AbstractUser):
    comment = models.TextField()
    nickname = models.CharField(max_length=30)
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to = "usr/%y")
    # 한 USER가 다른 USER를 follow를 하는 N:N 관계 설정
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    #self = 하나의 계정
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/need.png"

    def __str__(self):
        return self.nickname


from django.db import models
from acc.models import User
# Create your models here.
class Topic(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    voter = models.ManyToManyField(User, blank=True)
    ctime = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.subject
    
    def summary(self):
        if len(self.content) > 20:
            return self.content[:20] + "..."
        return self.content


class choice(models.Model):
    sub = models.ForeignKey(Topic, on_delete=models.CASCADE)
    select = models.CharField(max_length=100)
    comment = models.TextField()
    voter = models.ManyToManyField(User, blank=True)
    pic = models.ImageField(upload_to="vote/%y")

    def __str__(self):
        return f"{self.sub} : {self.select}"

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/need.png"
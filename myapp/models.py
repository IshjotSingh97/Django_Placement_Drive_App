from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    link = models.URLField(max_length=100)
    image = models.URLField(max_length=100)

class UserFeedback(models.Model):
    subject = models.CharField(max_length=100)
    feedback = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)


class Favourite(models.Model):
    uid = models.IntegerField()
    pid = models.IntegerField()
    posttitle = models.CharField(max_length=100)
    postlink = models.URLField(max_length=100)
    date = models.DateField(auto_now_add=True)

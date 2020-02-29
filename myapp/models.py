from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    link = models.URLField(max_length=100)
    image = models.ImageField(upload_to="media")
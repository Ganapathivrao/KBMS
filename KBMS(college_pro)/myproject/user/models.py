from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title=models.CharField(max_length=100)
    summary=models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now())
    body=models.TextField()

    def get_absolute_url(self):
        return reverse("user:articledetail",kwargs={'pk':self.pk})

class question(models.Model):
    your_name=models.CharField(max_length=100)
    your_question=models.CharField(max_length=300)
    upload_date=models.DateTimeField(default=datetime.now())

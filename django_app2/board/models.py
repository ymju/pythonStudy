from django.db import models

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=256)
    viewCount = models.IntegerField(default=0)

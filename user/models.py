from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    coin = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    cSelect = models.IntegerField(default=2)
    cSuccess = models.IntegerField(default=0)


class Attendance(models.Model):
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attDate = models.DateTimeField(auto_now_add=True)
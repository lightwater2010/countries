from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=100)
    currincies = models.CharField(max_length=150)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    all_names = models.CharField(max_length=200)
    google_maps = models.TextField()
    flag = models.TextField()
class Users(models.Model):
    name = models.CharField(max_length=30,verbose_name='Логин')
    email = models.TextField(verbose_name='Email')
    password = models.CharField(max_length=12,verbose_name='Пароль',unique=True)




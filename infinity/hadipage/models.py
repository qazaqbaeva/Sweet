from django.db import models

class zavedeniya(models.Model):
    title = models.CharField(max_length=255)
    content= models.TextField(blank=True)
    certificate = models.CharField(max_length=255)
    namazhana_omov=models.BooleanField(default=True)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create=models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
class User(models.Model):
    name=models.CharField(max_length=255)
    login=models.CharField(max_length=255)
    password=models.CharField(max_length=25)
    role_id=models.IntegerField()
class City(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
class Role(models.Model):
    role_id=models.IntegerField()
    role_name=models.CharField(max_length=255)
    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
class mymessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    mobile=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    message=models.TextField(max_length=500)
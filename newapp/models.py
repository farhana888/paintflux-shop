from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class  CustomUser(AbstractUser):
    # Add custom fields here,for example:
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True,unique=True)
    otp=models.IntegerField(null=True,blank=True)
    # exp_time=models.DateField(null=True,blank=True)
    exp_timee=models.DateTimeField(null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    phonenumber=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    profilepicture=models.ImageField(upload_to='images',null=True,blank=True)
    
    
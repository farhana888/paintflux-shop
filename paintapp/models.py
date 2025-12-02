from django.db import models
from newapp.models import CustomUser

# Create your models here.
class Upload(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)    
    image=models.ImageField(upload_to='uploadimages',null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='userdetails')

    def __str__(self):
       return str(self.name)
class Mycart(models.Model):
    art=models.ForeignKey(Upload,on_delete=models.CASCADE) 
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    date=models.DateTimeField(auto_now_add=True) 
    quantity=models.IntegerField(blank=True,null=True)

class Wishlist(models.Model):
    art = models.ForeignKey(Upload, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)   

class Follow(models.Model):
    follower=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='following')  
    following=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='followers')
    time = models.DateTimeField(auto_now_add=True)

class Order(models.Model):  
    city=models.CharField(max_length=100,null=True,blank=True) 
    pincode=models.IntegerField(null=True, blank=True)
    country=models.CharField(max_length=100,null=True,blank=True) 
    state=models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   



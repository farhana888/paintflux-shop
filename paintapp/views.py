from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    
    paints = Upload.objects.exclude(user=request.user)
    print(paints,'hlooooo')
    context={
        'paints':paints
    }
    return render(request, 'index.html', context)
    
def men(request):
    return render(request,'men.html')
def order(request):
    return render(request,'order-complete.html')
def product(request):
    return render(request,'product-detail.html')
def women(request):
    
    return render(request, 'women.html')
    
def about(request):
    return render(request,'about.html')
def addwish(request):
    return render(request,'add-to-wishlist.html')
def cart(request):
    return render(request,'cart.html')
def check(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')

def profile(request):
    current_user = request.user
    followers_count = Follow.objects.filter(following=current_user).count()
    following_count = Follow.objects.filter(follower=current_user).count()

    context = {
        
        'followers_count': followers_count,
        'following_count': following_count,
    }
    return render(request, 'profile.html', context)


   
def upload(request):
    return render(request,'upload.html')
def profilesave(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        profilepicture=request.FILES.get('profilepicture')
        email=request.POST.get('email')
        print(phone,address,profilepicture,email)
        cur_user=request.user
        usr=CustomUser.objects.get(username=cur_user.username)
        usr.phonenumber=phone
        usr.address=address
        usr.email=email
        if profilepicture:
            usr.profilepicture=profilepicture
        usr.save()
        return redirect('paintapp:profile')
    return render(request,'profilesave.html')
def uploadsave(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        category=request.POST.get('category')
        print(name,price,description,image,category)
        usr=request.user
        Upload.objects.create(name=name,price=price,image=image,description=description,category=category ,user=usr)
        return redirect('paintapp:index')
def myimages(request):
    myimages = Upload.objects.filter(user=request.user)
    print(myimages,'hlooooo')
    context={
        'myimages':myimages
    }  
    return render(request,'myimages.html',context)   
def edit(request,im_id):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        print(name,price,description,image) 
        my_item=Upload.objects.get(id=im_id)
        my_item.name=name
        my_item.price=price
        my_item.description=description
        if image:
            my_item.image=image
        my_item.save()
    return redirect('paintapp:myimages')   
def deleteimage(request,im_id):
    my_item=Upload.objects.get(id=im_id)
    my_item.delete()
    return redirect('paintapp:myimages')
def userupdate(request,im_id):
    my_item=Upload.objects.get(id=im_id)
    f=Follow.objects.filter(follower=request.user,following=CustomUser.objects.get(id=my_item.user.id))
    context= {
        'my_item':my_item,
        'f':f

    }
    
    return render(request,'userupdate.html',context)
def viewmore(request,u_id):
    artist=CustomUser.objects.get(id=u_id)
    arts=Upload.objects.filter(user=artist)
    context={
        'arts':arts
    }

    return render(request,'viewmore.html',context)
def mycart(request,item_id):
    myart=Upload.objects.get(id=item_id)
    user=request.user
    cart_irtem=Mycart.objects.filter(user=user,art=myart)
    
    if cart_irtem:
           messages.error(request,'item alredy exist')
           return redirect('paintapp:secondcart')
    else:
        item=Mycart.objects.create(art=myart,user=user)
        messages.success(request,'item added successfully')
        return redirect('paintapp:secondcart')

def secondcart(request):
    myproduct=Mycart.objects.filter(user=request.user)
    context={
        'myproduct':myproduct
    }
    return render(request,'mycart.html',context)



def wishlist(request,art_id):
    art = Upload.objects.get(id=art_id)
    user = request.user
    wishlist_item=Wishlist.objects.filter(user=user,art=art)
    if wishlist_item:
           messages.error(request,'alredy added to wishlist')
           return redirect('paintapp:viewwishlist')
    else:
        Wishlist.objects.create(user=user,art=art)
        messages.success(request,'item added to wishlist')
        return redirect('paintapp:viewwishlist')


def viewwishlist(request):
  wishlist = Wishlist.objects.filter(user=request.user)
  context = {
        'wishlist': wishlist
    }
  return render(request, 'wishlist.html', context)

def buy(request,item_id):
    buy_item= Upload.objects.get(id=item_id)
    try:
        citem=Mycart.objects.get(user=request.user,art=buy_item)
        
        quantity=citem.quantity
    except:
        quantity=1

    total_price=buy_item.price*quantity
    context= {
        'buy_item':buy_item,
        'total_price':total_price,
        'quantity':quantity

    }
    return render(request, 'buy.html', context)
def updatequantity(request,item_id,operator):
    buy_item= Upload.objects.get(id=item_id)

    print(item_id,operator)
    if operator=='minus':
        try:
            citem=Mycart.objects.get(art=buy_item,user=request.user)
            cq=citem.quantity
            if cq==1:
                messages.error(request,'cart Quantity cannot be less than 1')
                return redirect('paintapp:buy',item_id )
            else:
                citem.quantity=cq-1
                citem.save()
        except:
            messages.error(request,'cart Quantity cannot be less than 1')
            return redirect('paintapp:buy',item_id )
    if operator=='plus':
        try:
            citem=Mycart.objects.get(art=buy_item,user=request.user)
            cq=citem.quantity
            citem.quantity = cq + 1
            citem.save()
        except:
            Mycart.objects.create(art=buy_item,user=request.user,quantity=2)
        return redirect('paintapp:buy', item_id)
    
def followers(request):
    current_user=request.user
    followers=Follow.objects.filter(following=current_user)
    context={
        
        'followers': followers,

    }
    
    return render(request, 'followers.html',context)
def followings(request,):
    current_user=request.user
    following = Follow.objects.filter(follower=current_user)

    context = {
        
        'following': following,
    }
    return render(request, 'following.html', context)

  
def follow(request,user_id):
     user_profile = CustomUser.objects.get(id=user_id)
     current_user=request.user
     follow=Follow.objects.filter(follower=current_user,following=user_profile)
     if follow.exists():
        messages.error(request,"you are already following")
        
     else:
        
        Follow.objects.create(following=user_profile,follower=current_user)
        messages.success(request, "You are now following this user")
     return redirect('paintapp:userupdate',user_id)       
    
def unfollow(request,user_id):
    user_profile = CustomUser.objects.get(id=user_id)
    current_user = request.user

    unfollow= Follow.objects.filter(follower=current_user, following=user_profile)

    if unfollow:
        unfollow.delete()
        messages.success(request, "You unfollowed this user")
    else:
        messages.error(request, "You are not following this user")

    return redirect('paintapp:userupdate', user_id)
def chatboat(request):
    return render(request,'chatboat.html')
    
def ordernow(request,item_id):
    painting = Upload.objects.get(id=item_id)
    if request.method=='POST':
        pincode=request.POST.get('pincode')
        country=request.POST.get('country')
        city=request.POST.get('city')
        state=request.POST.get('state')
        print(pincode,country,city)
        usr=request.user
        Order.objects.create(pincode=pincode,country=country,city=city,state=state, user=usr)
        messages.success(request, "Your order has been placed successfully!")
        
        return redirect('paintapp:ordernow',item_id=item_id)
    context = {
        'painting': painting
    }
    return render(request, 'ordernow.html', context)
def placeorder (request, item_id):
     my_item=Upload.objects.get(id=item_id)
     context={
         'my_item':my_item
     }
     return render(request,'placeorder.html',context)
    
    


    

    
    
                



   
  
    
    
    
   

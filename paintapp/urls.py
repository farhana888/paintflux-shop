from django.urls import path
from.import views
from django.conf import settings 
from  django.conf.urls.static import static
app_name='paintapp'


urlpatterns = [
     path('',views.index,name='index'),
     path('mennnn',views.men,name='men'),
     path('orderrr',views.order,name='order-complete'),
     path('productt',views.product,name='product-detail'),
     path('womennn',views.women,name='women'),
     path('aboutt',views.about,name='about'),
     path('addd',views.addwish,name='add-to-wishlist'),
     path('carttt',views.cart,name='cart'),
     path('checkkkk',views.check,name='checkout'),
     path('contactt',views.contact,name='contact'),
     path('profile',views.profile,name='profile'),
     path('upload',views.upload,name='upload'),
     path('uploadsave',views.uploadsave,name='uploadsave'),
     path('profilesave',views.profilesave,name='profilesave'),
     path('myimages',views.myimages,name='myimages'),
     path('edit/<int:im_id>',views.edit,name='edit'),
     path('deleteimage/<int:im_id>',views.deleteimage,name='deleteimage'),
     path('userupdate/<int:im_id>',views.userupdate,name='userupdate'),
     path('viewmore/<int:u_id>',views.viewmore,name='viewmore'),
     path('mycart/<int:item_id>',views.mycart,name='mycart'),
     path('secondcart',views.secondcart,name='secondcart'),
     path('wishlist/<int:art_id>',views.wishlist,name='wishlist'),
     path('viewwishlist',views.viewwishlist,name='viewwishlist'),
     path('buy/<int:item_id>',views.buy,name='buy'),
     path('updatequantity/<int:item_id>/<str:operator>/', views.updatequantity, name='updatequantity'),
     path('followers',views.followers,name='followers'),
     path('followings',views.followings,name='following'),
     path('follow/<int:user_id>',views.follow,name='follow'),
     path('unfollow/<int:user_id>',views.unfollow,name='unfollow'),
     path('chatboat',views.chatboat,name='chatboat'),
     path('ordernow/<int:item_id>',views.ordernow,name='ordernow'),
     path('placeorder/<int:item_id>',views.placeorder,name='placeorder'),
    
     

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from.import views
from django.conf import settings 
from  django.conf.urls.static import static

app_name='newapp'

urlpatterns = [
     path('index',views.index,name='index'),
     path('nnnnn',views.four,name='404'),
     path('bbbb',views.blank,name='blank'),
     path('buuu',views.buttontmplt,name='button'),
     path('chhh',views.chart,name='chart'),
     path('eee',views.element,name='element'),
     path('fff',views.form,name='form'),
     path('',views.signin,name='signin'),
     path('sii',views.signup,name='signup'),
     path('taa',views.table,name='table'),
     path('tyyy',views.typography,name='typography'),
     path('wii',views.widget,name='widget'),
     path('otp',views.otp,name='otp'),
     path('passw',views.password,name='password'),
     path('pass',views.paintsignup,name='newpassword'),
     path('newww',views.newotp,name='newotp'),
     path('www',views.newpass,name='newpass'),
     path('signn',views.signinsave,name='signinsave'),
     path('viewuser',views.viewuser,name='viewuser'),
     path('viewdetails/<int:im_id>',views.viewdetails,name='viewdetails'),
     path('viewwork/<int:item_id>',views.viewwork,name='viewwork'),
     path('viewpurchase/<int:item_id>',views.viewpurchase,name='viewpurchase'),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

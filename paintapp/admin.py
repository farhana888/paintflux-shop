from django.contrib import admin
from.models import Upload
from .models import Mycart
from .models import Wishlist
from .models import Follow
from .models import Order

# Register your models here.
admin.site.register(Upload)
admin.site.register(Mycart)
admin.site.register(Wishlist)
admin.site.register(Follow)
admin.site.register(Order)


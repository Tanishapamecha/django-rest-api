from django.contrib import admin
from .models import Product
from .models import CustomUser
from .models import Task


# Register your models here.

admin.site.register(Product)
admin.site.register(CustomUser)
admin.site.register(Task)


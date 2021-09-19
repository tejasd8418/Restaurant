
from django.contrib import admin

# Register your models here.
from .models import foodItems, Contact, Orders

admin.site.register(foodItems)
admin.site.register(Contact)
admin.site.register(Orders)


from django.contrib import admin
from django.contrib.auth.models import Group
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.slider import Slider

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.site_header = 'PeriwinkleRose'
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Slider)

from django.contrib import admin
from .models import Products

# afficher les differentes table du model Product
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price','actif','slug')
# Register your models here.
admin.site.register(Products, AdminProduct)
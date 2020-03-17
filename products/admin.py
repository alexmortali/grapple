from django.contrib import admin
from .models import Category, Product 

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'featured']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'created', 'category', 'summary', 'price']

admin.site.register(Product, ProductAdmin)
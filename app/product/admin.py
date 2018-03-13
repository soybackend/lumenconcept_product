from django.contrib import admin

from .models import (Category, MediaResource, Product)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'active',)


@admin.register(MediaResource)
class MediaResourceAdmin(admin.ModelAdmin):
    list_display = ('label', 'product',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name',)

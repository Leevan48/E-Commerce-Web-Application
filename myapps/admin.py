from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import *

# Register your models here.

class CategoryAdmin(TranslatableAdmin):
    list_display = [
        'name'
    ]

class ProductAdmin(TranslatableAdmin):
    list_display = [
        'name', 'description'
    ]


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

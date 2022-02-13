from django.contrib import admin
from .models import Category,Book,products

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(products)
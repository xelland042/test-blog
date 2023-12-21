from django.contrib import admin

from shop.models import Product, Category, Specification, Type, SubType

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Specification)
admin.site.register(Type)
admin.site.register(SubType)

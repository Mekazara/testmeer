from django.contrib import admin

from apps.product.models import Product, ProductCategory

admin.site.register(Product)
admin.site.register(ProductCategory)
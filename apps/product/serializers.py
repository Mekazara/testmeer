from rest_framework import serializers
from apps.product.models import Product, ProductCategory

class ProductCategorySer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductReadableSer(serializers.ModelSerializer):
    product_category = ProductCategorySer()
    class Meta:
        model = Product
        fields = '__all__'

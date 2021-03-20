from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from apps.product.models import Product, ProductCategory
from apps.product.serializers import ProductSer, ProductCategorySer, ProductReadableSer
from rest_framework.viewsets import ModelViewSet

class ProdCatViewset(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySer

class ProdViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer

    def list(self, request, *args, **kwargs):
        product = self.queryset.all()
        serializer = ProductReadableSer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
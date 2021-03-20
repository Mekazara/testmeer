from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response

from apps.product.models import ProductCategory, Product


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.product_category = ProductCategory.objects.create(
            name='TestCategory'
        )
        self.product = Product.objects.create(
            name='Test',
            price=123,
            product_category=self.product_category
        )
    def get_product(self):
        product = Product.objects.get(
            name='Test',
            product_category=self.product_category
        )
        self.assertEqual(self.product, product)

    def get_category(self):
        product_category = ProductCategory.objects.get(
            name='TestCategory'
        )
        self.assertEqual(self.product_category, product_category)

    # def get_status(self):
    #     return Response(self.product, status=status.HTTP_201_CREATED)
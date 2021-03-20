from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.product.views import ProdCatViewset, ProdViewset

router = DefaultRouter()
router.register('product-category', ProdCatViewset)
router.register('products', ProdViewset)

urlpatterns = [
    path('', include(router.urls))
]
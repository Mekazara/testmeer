from rest_framework import routers
from django.urls import path, include
from apps.blog.views import PostViewset, AuthorViewset, PostCatViewset

router = routers.DefaultRouter()
router.register('post', PostViewset)
router.register('author', AuthorViewset)
router.register('post', PostCatViewset)

app_name = 'blog'

urlpatterns = [
    path('posts/', include(router.urls)),
]
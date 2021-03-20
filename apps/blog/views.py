from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PostSerializer, PostCategorySerializer, AuthorSerializer
from .models import Post, PostCategory, Author


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = PostSerializer


class PostCatViewset(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = PostSerializer

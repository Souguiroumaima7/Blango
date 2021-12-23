from django.contrib.auth.models import User
from rest_framework import generics

import blog.api.serializers
import blog.models

from Blog.api.permissions import AuthorModifyOrReadOnly , IsAdminUserForObject
from Blog.api.serializers import PostSerializer , UserSerializer , PostDetailSerializer
from Blog.models import Post
import blog.api.permissions



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly]
    # leave other attributes as is
permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer

import blog.api.serializers
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


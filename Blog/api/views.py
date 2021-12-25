from django.contrib.auth.models import User
from requests import Response
from rest_framework import generics

import blog.api.serializers
import blog.models
from rest_framework.decorators import action

from Blog.api.filters import PostFilterSet
from Blog.api.permissions import AuthorModifyOrReadOnly , IsAdminUserForObject
from Blog.api.serializers import PostSerializer , UserSerializer , PostDetailSerializer , TagSerializer
from Blog.models import Post , Tag
import blog.api.permissions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, viewsets
import blog.api.filters


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


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(vary_on_cookie)
    @action(methods=["get"], detail=False, name="Posts by the logged in user")
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer


from rest_framework.decorators import action
from rest_framework.response import Response

class TagViewSet(viewsets.ModelViewSet):
    # existing attributes omitted

    @action(methods=["get"], detail=True, name="Posts with the Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        post_serializer = PostSerializer(
            tag.posts, many=True, context={"request": request}
        )
        return Response(post_serializer.data)
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)

        page = self.paginate_queryset(posts)

        if page is not None:
            serializer = PostSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)

    def posts(self, request, pk=None):
        tag = self.get_object()
        page = self.paginate_queryset(tag.posts)
        if page is not None:
            post_serializer = PostSerializer(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(post_serializer.data)
        post_serializer = PostSerializer(
            tag.posts, many=True, context={"request": request}
        )
        return Response(post_serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    filterset_class = PostFilterSet
    # filterset_fields can be removed
    # other existing attributes and methods omitted
from django.db.models import Q
from django.utils import timezone


def get_queryset(self) :
    if self.request.user.is_anonymous :
        # published only
        return self.queryset.filter(published_at__lte=timezone.now())

    if not self.request.user.is_staff :
        # allow all
        return self.queryset

    # filter for own or
    return self.queryset.filter(
        Q(published_at__lte=timezone.now()) | Q(author=self.request.user)
    )
    @method_decorator(cache_page(120))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)

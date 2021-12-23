from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns

import blog.api.views

from Blog.api.api_views import PostDetail
from Blog.api.views import PostList

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("api/v1/", include("blog.api.urls"))


]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path("auth/", include("rest_framework.urls")),
]
from rest_framework.authtoken import views
urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token)
]

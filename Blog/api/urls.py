import debug_toolbar
from django.conf import settings
from django.urls import path , include , re_path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Blog.api.api_views import PostDetail
from Blog.api.views import PostList , UserDetail , TagViewSet , PostViewSet

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
urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

import drf_yasg.views
import os
schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
from rest_framework.routers import DefaultRouter
import blog.api.views
router = DefaultRouter()
router.register("tags", TagViewSet)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    # ... other patterns omitted
    path("", include(router.urls)),
]

path("posts/" , PostList.as_view() , name="api_post_list") ,
path("posts/<int:pk>" , PostDetail.as_view() , name="api_post_detail") ,
urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]
router.register("posts", PostViewSet)

path(
    "posts/by-time/<str:period_name>/" ,
    PostViewSet.as_view({"get" : "list"}) ,
    name="posts-by-time" ,
) ,
path("", include(router.urls)),

path("jwt/" , TokenObtainPairView.as_view() , name="jwt_obtain_pair") ,
path("jwt/refresh/" , TokenRefreshView.as_view() , name="jwt_refresh") ,

from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from os import path

from rest_framework.urlpatterns import format_suffix_patterns

from Blog.api.api_views import post_detail
from Blog.api_views import post_list

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>", post_detail, name="api_post_detail"),
]


urlpatterns = format_suffix_patterns(urlpatterns)

from django.contrib import admin

from Blog.models import Tag , Post , AuthorProfile
admin.site.register(Tag)


class Post(admin.ModelAdmin):
 prepopulated_fields = {"slug": ("title",)}
 admin.site.register(Post)


admin.site.register(AuthorProfile)



from django.contrib import admin
from django.contrib.auth import get_user_model
from post.models import Post, Tag, Comment

User = get_user_model()

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_deleted']

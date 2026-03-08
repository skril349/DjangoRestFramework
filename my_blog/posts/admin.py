from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'order', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
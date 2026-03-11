from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'post', 'user')
    list_filter = ('created_at', 'post', 'user')    
    search_fields = ('content', 'post__title', 'user__username')
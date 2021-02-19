from django.contrib import admin

from .models import Comment
from itstore.base_admin import BaseOwnerAdmin

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'thread',
        'user',
        'body',
        'timestamp',
    )


admin.site.register(Comment, CommentAdmin)

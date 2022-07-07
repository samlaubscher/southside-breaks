from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle_one',
        'subtitle_two',
        'subtitle_three',
        'body_one',
        'body_two',
        'body_three',
        'body_four',
        'main_image_url',
        'main_image',
        'image_two_url',
        'image_two',
        'image_three_url',
        'image_three',
        'image_four_url',
        'image_four',
    )

    ordering = ('title',)


admin.site.register(Blog, BlogAdmin)
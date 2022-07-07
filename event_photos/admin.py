from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'event',
        'image_url',
        'image',
    )

    ordering = ('event',)


admin.site.register(Photo, PhotoAdmin)
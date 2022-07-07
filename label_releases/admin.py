from django.contrib import admin
from .models import LabelRelease


class LabelReleaseAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'description',
        'number',
        'release_date',
        'artist_link',
        'soundcloud_link',
        'beatport_link',
        'image_url',
        'image',
        'timestamp',
        'posted_by',
    )

    ordering = ('number',)


admin.site.register(LabelRelease, LabelReleaseAdmin)
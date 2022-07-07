from django.contrib import admin
from .models import GuestMix


class GuestMixAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'description',
        'number',
        'artist_link',
        'soundcloud_mix_link',
        'image_url',
        'image',
        'timestamp',
        'posted_by',
    )

    ordering = ('number',)


admin.site.register(GuestMix, GuestMixAdmin)
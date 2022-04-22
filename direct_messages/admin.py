from django.contrib import admin
from .models import DirectMessage


class DirectMessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'receiver',
        'body',
        'timestamp',
        'read',
    )

    ordering = ('timestamp',)


admin.site.register(DirectMessage, DirectMessageAdmin)
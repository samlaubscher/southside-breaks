from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'venue',
        'event_date',
        'ticket_prices',
        'ticket_link',
        'facebook_link',
        'set_times',
        'image_url',
        'image',
        'timestamp',
        'posted_by',
    )

    ordering = ('event_date',)


admin.site.register(Event, EventAdmin)
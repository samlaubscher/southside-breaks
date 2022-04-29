from django.contrib import admin
from .models import Thread, Topic


class ThreadAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'topic',
        'user',
        'timestamp',
    )

    ordering = ('title',)


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Topic, TopicAdmin)
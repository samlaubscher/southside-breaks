from django.contrib import admin
from .models import TeamMember


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'artist_name',
        'description',
        'soundcloud_link',
        'beatport_link',
        'image_url',
        'image',
    )

    ordering = ('artist_name',)


admin.site.register(TeamMember, TeamMemberAdmin)
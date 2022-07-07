from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TeamMember(models.Model):
    name = models.CharField(max_length=70, blank=False, null=False)
    artist_name = models.CharField(max_length=70, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=False, null=False)
    soundcloud_link = models.URLField(max_length=150, null=True, blank=True)
    beatport_link = models.URLField(max_length=150, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    class Meta:
        ordering = ['artist_name']

    def __str__(self):
        return self.name
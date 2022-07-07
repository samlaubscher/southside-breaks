from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from django.utils import timezone
import math

class Photo(models.Model):
    """ A model for Event Photos """
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='photo'
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    class Meta:
        ordering = ['event']

    def __str__(self):
        return 'Photo from {}'.format(self.event)
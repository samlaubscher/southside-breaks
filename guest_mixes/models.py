from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math


class GuestMix(models.Model):
    artist = models.CharField(max_length=70, blank=False, null=False)
    description = models.TextField(max_length=5000, blank=False, null=False)
    number = models.DecimalField(max_digits=4, decimal_places=0, blank=False, null=False)
    artist_link = models.URLField(max_length=150, null=True, blank=True)
    soundcloud_mix_link = models.URLField(max_length=150, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)


    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Guest Mixes'

    def __str__(self):
        return self.number
    
    def whenpublished(self):
        now = timezone.now()
        
        diff = now - self.timestamp

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

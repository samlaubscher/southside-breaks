from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math


class Blog(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    subtitle_one = models.CharField(max_length=300, blank=True, null=True)
    subtitle_two = models.CharField(max_length=300, blank=True, null=True)
    subtitle_three = models.CharField(max_length=300, blank=True, null=True)
    body_one = models.TextField(max_length=5000, blank=False, null=False)
    body_two = models.TextField(max_length=5000, blank=True, null=True)
    body_three = models.TextField(max_length=5000, blank=True, null=True)
    body_four = models.TextField(max_length=5000, blank=True, null=True)
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    image_two_url = models.URLField(max_length=1024, null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three_url = models.URLField(max_length=1024, null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    image_four_url = models.URLField(max_length=1024, null=True, blank=True)
    image_four = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title
    
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

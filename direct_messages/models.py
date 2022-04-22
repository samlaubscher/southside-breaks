from django.db import models
from django.contrib.auth.models import User


class DirectMessage(models.Model):
    sender = models.ForeignKey(User, null=False, blank=False,
                                 on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, null=False, blank=False,
                                 on_delete=models.CASCADE, related_name='receiver')
    body = models.TextField(max_length=3000, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return 'Message'
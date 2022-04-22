from django.conf import settings
from .models import DirectMessage


def inbox_unread(request):

    user = request.user
    
    if user.is_authenticated:
        direct_messages = DirectMessage.objects.filter(receiver=request.user)
        unread = direct_messages.filter(read=False)

        context = {
            'unread': unread,
        }
        return context
    else:
        return {
            'unread': None
        }

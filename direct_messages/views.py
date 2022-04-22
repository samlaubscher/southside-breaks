from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import DirectMessage


def inbox(request):
    """ A view to return inbox """
    
    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))

    direct_messages = DirectMessage.objects.filter(receiver=request.user)

    context = {
        'direct_messages': direct_messages,
    }

    return render(request, 'direct_messages/inbox.html', context)

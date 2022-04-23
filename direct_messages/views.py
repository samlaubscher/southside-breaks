from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import DirectMessage
from .forms import SendMessageForm, ReplyToMessageForm
from datetime import datetime


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


def sent_messages(request):
    """ A view to return sent messages """
    
    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))

    direct_messages = DirectMessage.objects.filter(sender=request.user)

    context = {
        'direct_messages': direct_messages,
    }

    return render(request, 'direct_messages/sent_messages.html', context)


def view_message(request, direct_message_id):
    """ A view to view a message """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))
    
    direct_message = get_object_or_404(DirectMessage, pk=direct_message_id)
    recipient = direct_message.receiver

    if recipient == request.user:
        direct_message.read = True
        direct_message.save()

    template = 'direct_messages/view_message.html'

    context = {
        'direct_message': direct_message
    }

    return render(request, template, context)


def send_message(request):
    """ A view to send a message """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))

    sender = request.user
    form = None

    if request.method == 'POST':
        form = SendMessageForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.sender = sender
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully sent message!')
            return redirect(reverse('messages'))
    else:
        form = SendMessageForm()

    template = 'direct_messages/send_message.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def reply_to_message(request, direct_message_id):
    """ A view to send a message """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))

    direct_message = get_object_or_404(DirectMessage, pk=direct_message_id)
    recipient = direct_message.sender
    sender = request.user
    form = None

    if request.method == 'POST':
        form = ReplyToMessageForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.receiver = recipient
            form.sender = sender
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully sent message!')
            return redirect(reverse('sent_messages'))
    else:
        form = ReplyToMessageForm()

    template = 'direct_messages/reply_to_message.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
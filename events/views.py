from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Event
from .forms import EventForm
from datetime import datetime


def all_events(request):
    """ A view to return all events """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'threads/threads.html', context)


def view_event(request, event_id):
    """ A view to view an event """
    
    event = get_object_or_404(Event, pk=event_id)

    template = 'events/view_event.html'

    context = {
        'event': event,
    }

    return render(request, template, context)


def create_event(request):
    """ A view to create an event """

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    user = request.user
    form = None

    if request.method == 'POST':
        form = EventForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.posted_by = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully posted event!')
            return redirect('view_event', form.pk)
    else:
        form = EventForm()

    template = 'events/create_event.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_event(request, event_id):
    """ Edit an event """
    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    user = event.posted_by

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('view_event', args=[event.id]))
        else:
            messages.error(request, 'Failed to update event. \
                Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


def delete_event(request, event_id):
    """ A view to delete an event """

    event = get_object_or_404(Event, pk=event_id)

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import GuestMix
from .forms import GuestMixForm
from datetime import datetime


def all_guest_mixes(request):
    """ A view to return all guest mixes """

    guest_mixes = GuestMix.objects.all().order_by('-number')

    context = {
        'guest_mixes': guest_mixes,
    }

    return render(request, 'guest_mixes/guest_mixes.html', context)


def view_guest_mix(request, guest_mix_id):
    """ A view to view a guest mix """
    
    guest_mix = get_object_or_404(GuestMix, pk=guest_mix_id)

    template = 'guest_mixes/view_guest_mix.html'

    context = {
        'guest_mix': guest_mix,
    }

    return render(request, template, context)


def create_guest_mix(request):
    """ A view to create a guest_mix """

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    user = request.user
    form = None

    if request.method == 'POST':
        form = GuestMixForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.posted_by = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully posted guest mix!')
            return redirect('view_guest_mix', form.pk)
    else:
        form = GuestMixForm()

    template = 'guest_mixes/create_guest_mix.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_guest_mix(request, guest_mix_id):
    """ Edit a guest_mix """
    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    guest_mix = get_object_or_404(GuestMix, pk=guest_mix_id)
    user = guest_mix.posted_by

    if request.method == 'POST':
        form = GuestMixForm(request.POST, request.FILES, instance=guest_mix)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated guest mix!')
            return redirect(reverse('view_guest_mix', args=[guest_mix.id]))
        else:
            messages.error(request, 'Failed to update guest mix. \
                Please ensure the form is valid.')
    else:
        form = GuestMixForm(instance=guest_mix)
        messages.info(request, f'You are editing {guest_mix.artist}\'s guest mix')

    template = 'guest_mixes/edit_guest_mix.html'
    context = {
        'form': form,
        'guest_mix': guest_mix,
    }

    return render(request, template, context)


def delete_guest_mix(request, guest_mix_id):
    """ A view to delete a guest mix """

    guest_mix = get_object_or_404(GuestMix, pk=guest_mix_id)

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    guest_mix.delete()
    messages.success(request, 'Guest mix deleted!')
    return redirect(reverse('guest_mixes'))

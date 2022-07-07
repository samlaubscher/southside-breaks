from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Photo
from .forms import PhotoForm
from datetime import datetime


def event_photos(request):
    """ A view to return all event photos """

    photos = Photo.objects.all().order_by('event')

    context = {
        'photos': photos,
    }

    return render(request, 'event_photos/event_photos.html', context)


def view_photo(request, photo_id):
    """ A view to view a photo """
    
    photo = get_object_or_404(Photo, pk=photo_id)

    template = 'event_photos/view_photo.html'

    context = {
        'photo': photo,
    }

    return render(request, template, context)


def upload_photo(request):
    """ A view to upload a photo """

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    form = None

    if request.method == 'POST':
        form = PhotoForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully uploaded photo!')
            return redirect('view_photo', form.pk)
    else:
        form = PhotoForm()

    template = 'event_photos/upload_photo.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_photo(request, photo_id):
    """ A view to delete a photo """

    photo = get_object_or_404(Photo, pk=photo_id)

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    photo.delete()
    messages.success(request, 'Photo deleted!')
    return redirect(reverse('event_photos'))

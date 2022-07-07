from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import LabelRelease
from .forms import LabelReleaseForm
from datetime import datetime


def all_releases(request):
    """ A view to return all label releases """

    releases = LabelRelease.objects.all().order_by('-number')

    context = {
        'releases': releases,
    }

    return render(request, 'label_releases/label_releases.html', context)


def view_release(request, release_id):
    """ A view to view a label release """
    
    release = get_object_or_404(LabelRelease, pk=release_id)

    template = 'label_releases/view_release.html'

    context = {
        'release': release,
    }

    return render(request, template, context)


def create_release(request):
    """ A view to create a label release """

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    user = request.user
    form = None

    if request.method == 'POST':
        form = LabelReleaseForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.posted_by = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully posted label release!')
            return redirect('view_release', form.pk)
    else:
        form = LabelReleaseForm()

    template = 'label_releases/create_release.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_release(request, release_id):
    """ Edit a label release """
    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    release = get_object_or_404(LabelRelease, pk=release_id)
    user = release.posted_by

    if request.method == 'POST':
        form = LabelReleaseForm(request.POST, request.FILES, instance=release)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated label release!')
            return redirect(reverse('view_release', args=[release.id]))
        else:
            messages.error(request, 'Failed to update label release. \
                Please ensure the form is valid.')
    else:
        form = LabelReleaseForm(instance=release)
        messages.info(request, f'You are editing release number {release.number}')

    template = 'label_release/edit_release.html'
    context = {
        'form': form,
        'release': release,
    }

    return render(request, template, context)


def delete_release(request, release_id):
    """ A view to delete a label release """

    release = get_object_or_404(LabelRelease, pk=release_id)

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    release.delete()
    messages.success(request, 'Label release deleted!')
    return redirect(reverse('releases'))

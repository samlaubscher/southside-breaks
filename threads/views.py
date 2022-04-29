from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Thread
from .forms import CommentForm, ThreadForm
from datetime import datetime


def all_threads(request):
    """ A view to return all threads """
    
    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))

    threads = Thread.objects.all()

    context = {
        'threads': threads,
    }

    return render(request, 'threads/threads.html', context)


def view_thread(request, thread_id):
    """ A view to view a thread """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))
    
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = thread.comment.all()
    user = request.user
    thread_user = thread.user
    form = None

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.thread = thread
            form.user = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('view_thread', args=[thread.id]))
    else:
        form = CommentForm()

    template = 'threads/view_thread.html'

    context = {
        'thread': thread,
        'comments': comments,
        'form': form,
        'thread_user': thread_user,
    }

    return render(request, template, context)


def create_thread(request):
    """ A view to return all threads """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be a registered user to do that!')
        return redirect(reverse('home'))

    user = request.user
    form = None

    if request.method == 'POST':
        form = ThreadForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully posted!')
            return redirect('view_thread', form.pk)
    else:
        form = ThreadForm()

    template = 'threads/create_thread.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_thread(request, thread_id):
    """ Edit a thread """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can do that!')
        return redirect(reverse('home'))

    thread = get_object_or_404(Thread, pk=thread_id)
    user = thread.user

    if not request.user.is_superuser and not request.user == user:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('view_thread', args=[thread.id]))
        else:
            messages.error(request, 'Failed to update post. \
                Please ensure the form is valid.')
    else:
        form = ThreadForm(instance=thread)
        messages.info(request, f'You are editing {thread.title}')

    template = 'threads/edit_thread.html'
    context = {
        'form': form,
        'thread': thread,
    }

    return render(request, template, context)


def delete_thread(request, thread_id):
    """ A view to delete a thread """

    thread = get_object_or_404(Thread, pk=thread_id)
    user = thread.user

    if not request.user.is_superuser and not request.user == user:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    thread.delete()
    messages.success(request, 'Thread deleted!')
    return redirect(reverse('threads'))

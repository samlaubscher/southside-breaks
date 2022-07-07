from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog
from .forms import BlogForm
from datetime import datetime


def blogs(request):
    """ A view to return all blogs """

    blogs = Blog.objects.all().order_by('-timestamp')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)


def view_blog(request, blog_id):
    """ A view to view a blog post """
    
    blog = get_object_or_404(Blog, pk=blog_id)

    template = 'blogs/view_blog.html'

    context = {
        'blog': blog,
    }

    return render(request, template, context)


def create_blog(request):
    """ A view to create a blog post """

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    user = request.user
    form = None

    if request.method == 'POST':
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.posted_by = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully posted blog post!')
            return redirect('view_blog', form.pk)
    else:
        form = BlogForm()

    template = 'blogs/create_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_blog(request, blog_id):
    """ Edit a blog post """
    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    user = blog.posted_by

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('view_blog', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog post. \
                Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing blog "{blog.title}"')

    template = 'blogs/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


def delete_blog(request, blog_id):
    """ A view to delete a blog post """

    blog = get_object_or_404(Blog, pk=blog_id)

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    blog.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('blogs'))

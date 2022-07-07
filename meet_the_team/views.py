from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import TeamMember
from .forms import TeamMemberForm
from datetime import datetime


def team_members(request):
    """ A view to return all team members """

    members = TeamMember.objects.all()

    context = {
        'members': members,
    }

    return render(request, 'meet_the_team/members.html', context)


def view_member(request, member_id):
    """ A view to view a team member """
    
    member = get_object_or_404(TeamMember, pk=member_id)

    template = 'meet_the_team/view_member.html'

    context = {
        'member': member,
    }

    return render(request, template, context)


def create_member(request):
    """ A view to create a team member """

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    user = request.user
    form = None

    if request.method == 'POST':
        form = TeamMemberForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.posted_by = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully posted label release!')
            return redirect('view_member', form.pk)
    else:
        form = TeamMemberForm()

    template = 'meet_the_team/create_member.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_member(request, member_id):
    """ Edit a team member """
    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this!')
        return redirect(reverse('home'))

    member = get_object_or_404(TeamMember, pk=member_id)

    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated team member!')
            return redirect(reverse('view_member', args=[member.id]))
        else:
            messages.error(request, 'Failed to update team member. \
                Please ensure the form is valid.')
    else:
        form = TeamMemberForm(instance=member)
        messages.info(request, f'You are editing team member {member.name}')

    template = 'meet_the_team/edit_member.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)


def delete_member(request, member_id):
    """ A view to delete a team member """

    member = get_object_or_404(TeamMember, pk=member_id)

    if not request.user.is_authenticated and not request.user.is_superuser:
        messages.error(request, 'Nice try. You are not allowed to do that!')
        return redirect(reverse('home'))
    
    member.delete()
    messages.success(request, 'Team member deleted!')
    return redirect(reverse('team_members'))

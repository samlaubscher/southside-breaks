from django import forms
from .models import TeamMember
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class TeamMemberForm(forms.ModelForm):
    """ Full new team member form """

    class Meta:
        model = TeamMember
        fields = [
            'name',
            'artist_name',
            'description',
            'soundcloud_link',
            'beatport_link',
            'image_url',
            'image',
        ]
    
    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['name'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['description'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
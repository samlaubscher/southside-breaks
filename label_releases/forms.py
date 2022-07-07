from django import forms
from .models import LabelRelease
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class LabelReleaseForm(forms.ModelForm):
    """ Full new label release form """

    class Meta:
        model = LabelRelease
        fields = [
            'artist',
            'description',
            'number',
            'release_date',
            'artist_link',
            'soundcloud_link',
            'beatport_link',
            'image_url',
            'image',
        ]
    
    def __init__(self, *args, **kwargs):
        super(LabelReleaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['artist'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['description'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
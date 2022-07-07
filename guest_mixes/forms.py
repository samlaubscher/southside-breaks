from django import forms
from .models import GuestMix
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class GuestMixForm(forms.ModelForm):
    """ Full new guest mix form """

    class Meta:
        model = GuestMix
        fields = [
            'artist',
            'description',
            'number',
            'artist_link',
            'soundcloud_mix_link',
            'image_url',
            'posted_by',
        ]
    
    def __init__(self, *args, **kwargs):
        super(GuestMixForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['artist'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['description'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
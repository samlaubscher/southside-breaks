from django import forms
from .models import Photo
from events.models import Event
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class PhotoForm(forms.ModelForm):
    """ Upload photo form """

    event = forms.ModelChoiceField(queryset=Event.objects.all(), initial=0)

    class Meta:
        model = Photo
        fields = [
            'event',
            'image_url',
            'image',
        ]
    
    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['title'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['body_one'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
from django import forms
from .models import Event
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class EventForm(forms.ModelForm):
    """ Full new event form """

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'venue',
            'event_date',
            'ticket_prices',
            'ticket_link',
            'facebook_link',
            'set_times',
            'image_url',
            'posted_by',
        ]
    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['title'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['description'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['venue'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['event_date'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['ticket_prices'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['ticket_link'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['facebook_link'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['set_times'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['image_url'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
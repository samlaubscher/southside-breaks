from django import forms
from django.contrib.auth.models import User
from .models import DirectMessage
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class SendMessageForm(forms.ModelForm):
    """ Full new message form """

    receiver = forms.ModelChoiceField(queryset=User.objects.all(), initial=0)

    class Meta:
        model = DirectMessage
        fields = [
            'receiver',
            'body',
        ]
    
    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['body'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['receiver'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')


class ReplyToMessageForm(forms.ModelForm):
    """ Full reply to message form """

    class Meta:
        model = DirectMessage
        fields = [
            'body',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')

from django import forms
from .models import Thread, Topic
from comments.models import Comment
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class ThreadForm(forms.ModelForm):
    """ Full new thread form """

    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), initial=0)

    class Meta:
        model = Thread
        fields = [
            'title',
            'body',
            'topic',
        ]
    
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['title'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['body'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['topic'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')


class CommentForm(forms.ModelForm):
    """ Full comment form """

    class Meta:
        model = Comment
        fields = [
            'body',
        ]
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['body'].widget.attrs.update(style='width:100%;max-height:100px;font-size:15px;background-color:#ffffff17;color:#ade1ad;')

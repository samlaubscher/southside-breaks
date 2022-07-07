from django import forms
from .models import Blog
from crispy_forms.helper import FormHelper
from django.forms import ModelChoiceField


class BlogForm(forms.ModelForm):
    """ Full new blog form """

    class Meta:
        model = Blog
        fields = [
            'title',
            'main_image_url',
            'main_image',
            'body_one',
            'subtitle_one',
            'image_two_url',
            'image_two',
            'body_two',
            'subtitle_two',
            'image_three_url',
            'image_three',
            'body_three',
            'subtitle_three',
            'image_four_url',
            'image_four',
            'body_four',
        ]
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.fields['title'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
        self.fields['body_one'].widget.attrs.update(style='width:100%;font-size:15px;background-color:#ffffff17;color:#ade1ad;')
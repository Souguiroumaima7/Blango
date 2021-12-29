from django import forms

import blog.models
from django.template.defaulttags import comment


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ["content"]

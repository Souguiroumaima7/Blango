from django import forms

from blog.models import comment


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ["content"]

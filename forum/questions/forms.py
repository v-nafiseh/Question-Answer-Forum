from django import forms
from . import models
class DisplayForm(forms.ModelForm):

    class Meta:
        model = models.Question
        fields = ('title', 'content')
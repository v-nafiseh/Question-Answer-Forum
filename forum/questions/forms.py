from django import forms
from . import models
# from ckeditor.widgets import CKEditorWidget

class DisplayForm(forms.ModelForm):

    # title = forms.CharField(
    #     widget=forms.CharField(), 
        

    # )

    class Meta:
        model = models.Question
        fields = ['title', 'content', 'tags', ]
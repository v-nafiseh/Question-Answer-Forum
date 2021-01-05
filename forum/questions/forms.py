from django import forms
from . import models
from django.contrib.auth.models import User
# from ckeditor.widgets import CKEditorWidget

class DisplayForm(forms.ModelForm):

    # title = forms.CharField(
    #     widget=forms.CharField(), 
    # )

    class Meta:
        model = models.Question
        fields = ['title', 'content', 'tags', ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]        
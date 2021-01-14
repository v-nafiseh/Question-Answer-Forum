from django import forms
from . import models
from django.contrib.auth.models import User
# from ckeditor.widgets import CKEditorWidget

class DisplayForm(forms.ModelForm):

    # title = forms.CharField(
    #     widget=forms.CharField(), 
    # )

    tags = forms.CharField(max_length= 100,  required = False, widget=forms.Textarea(attrs={"rows":3, "cols":15}))

    class Meta:
        model = models.Question
        fields = ['title', 'content', 'category', ]

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', ]    

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['content', ]         
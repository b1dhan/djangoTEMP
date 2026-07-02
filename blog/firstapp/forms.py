from django import forms
from .models import Posts

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["author","category","title","image_url","status","content","slug"]
        # VVV this does the work of <input type="text" placeholder="enter author name">
        widgets={
            "author":forms.TextInput(attrs={
                "placeholder":"Enter Author Name",
                "max_length":30,
                "class":30,
                "class":"form-control"
            }),
            "category":forms.Select(attrs={
                "placeholder":"Select"
            }),
            "title":forms.TextInput(attrs={
                "placeholder":"Enter Post Title"
            }),
            "image_url":forms.URLInput(attrs={
                "placeholder":"image.com"
            }),
            "status":forms.TextInput(),
            "content":forms.Textarea(attrs={
                "placeholder":"Enter Post Content",
                "row":2,
                "max_length":1000,
            }),
            "slug":forms.TextInput(attrs={
                "placeholder":"Enter Post Slug"
            })
        }
        

from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username','password','confirm_password']

    def clean():
        cleaned_data=super().clean()
        password=cleaned_data['password']
        confirm_password=cleaned_data['confirm_password']

        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Password did not match.")
        return cleaned_data
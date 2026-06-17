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
        
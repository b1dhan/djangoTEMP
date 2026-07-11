from django import forms
from .models import Posts

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["category","title","image_url","status","content","slug"]
        # VVV this does the work of <input type="text" placeholder="enter author name">
        widgets={
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
        
# before adding email
# from django.contrib.auth.models import User
# class SignUpForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput, required=True)
#     email = forms.EmailField(widget=forms.EmailInput, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)
#     confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

#     class Meta:
#         model = User
#         fields = ['username','password','confirm_password']   

#     def clean(self):
#         cleaned_data=super().clean()
#         password=cleaned_data['password']
#         confirm_password=cleaned_data['confirm_password']

#         if password and confirm_password and password!=confirm_password:
#             raise forms.ValidationError("Password did not match.")
#         return cleaned_data

# after adding email,validations
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, required=True)
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords did not match.")
        return cleaned_data
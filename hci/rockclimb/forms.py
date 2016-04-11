from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, EmailField, TextInput, Select, Form, CharField
from models import *

class UserCreateForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ClimbCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClimbCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Climb
        fields = '__all__'
        exclude = [
            'user'
        ]
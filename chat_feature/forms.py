from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import CharField
from django.forms.widgets import Textarea
from django.core import validators
from django.contrib.auth.models import User

class contact_creation_form(UserCreationForm):
    study = forms.CharField()
    no = forms.CharField()
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","first_name","last_name")

class chat_create_form(forms.Form):
    room_name = forms.CharField()
    emails = forms.CharField(widget=Textarea)
    def clean_emails(self):
        data = self.cleaned_data.get('emails')
        value = data.strip()
        value = value.strip('\n')
        if not value:
            value = []
        value = value.split('\n')
        temp = ''
        for i in value:
            validators.validate_email(i)
            user = User.objects.filter(email=i)
            if len(user) == 0:
                temp = i
                break
        if len(temp) != 0:
            raise ValidationError(f'The email {temp} does not exist')
        return value

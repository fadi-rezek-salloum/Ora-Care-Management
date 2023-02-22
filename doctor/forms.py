from django.contrib.auth.forms import  AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
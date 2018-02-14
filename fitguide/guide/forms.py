from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    phone_number = forms.IntegerField(required = True)

    class Meta:
        model = User
        fields = (
                'username',
                'first_name',
                'last_name',
                'email',
                'phone_number',
                'password1',
                'password2',
        )

        def save(self,commit = True):
            user = super(RegisterForm,self).save(commit = False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.phone_number = self.cleaned_data['phone_number']
            if commit:
                user.save()
            return user


class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
                'first_name',
                'last_name',
                'email',
                'password',
        )

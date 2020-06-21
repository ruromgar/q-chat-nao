from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.models import Group, User


class RegistrationFormWithGroup(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a comboBox with groups
    """
    group = forms.ModelChoiceField(queryset=Group.objects.all())


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': ('Nombre'),
            'last_name': ('Apellidos'),
            'email': ('Email'),
        }

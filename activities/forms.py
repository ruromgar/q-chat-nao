from django import forms
from .models import *


class Activity01Form(forms.ModelForm):
    class Meta:
        model = Activity01
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity01Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()


class Activity02Form(forms.ModelForm):
    class Meta:
        model = Activity02
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity02Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()


class Activity03Form(forms.ModelForm):
    class Meta:
        model = Activity03
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity03Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()


class Activity04Form(forms.ModelForm):
    class Meta:
        model = Activity04
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity04Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()


class Activity05Form(forms.ModelForm):
    class Meta:
        model = Activity05
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity05Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()


class Activity06Form(forms.ModelForm):
    class Meta:
        model = Activity06
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity06Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()


class Activity07Form(forms.ModelForm):
    class Meta:
        model = Activity07
        exclude = ('therapist', 'comments', 'date')

    def __init__(self, *args, **kwargs):
        super(Activity07Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()

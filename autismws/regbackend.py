from registration.backends.default.views import RegistrationView

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory

from .forms import RegistrationFormWithGroup

from .utils import get_user_prediction


class MyRegistrationView(RegistrationView):

    form_class = RegistrationFormWithGroup

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        user_group = form_class.cleaned_data['group']
        new_user.groups.add(user_group)
        return new_user


def edit_user(request, pk):

    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    profile_formset = inlineformset_factory(
        User,
        UserProfile,
        exclude=('added_to_dataset',),
        can_delete=False,
    )
    formset = profile_formset(instance=user)

    if request.method == "POST":
        user_form = UserProfileForm(request.POST, instance=user)
        formset = profile_formset(request.POST, instance=user)

        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            formset = profile_formset(request.POST, instance=created_user)

            if formset.is_valid():
                created_user.save()
                formset.save()
                return HttpResponseRedirect('/')

    return render(request, "profile.html", {
        "noodle": pk,
        "noodle_form": user_form,
        "formset": formset,
        "answers": get_user_prediction(pk)
    })


def user_list(request):

    patients = User.objects.filter(groups__name='Patients')

    return render(
        request,
        'users.html',
        {
            'patients': patients,
        }
    )

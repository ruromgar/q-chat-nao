from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User

from .forms import Activity01Form, Activity02Form, Activity03Form, Activity04Form,\
    Activity05Form, Activity06Form, Activity07Form
from .utils import nao_rest, nao_wake_up

import subprocess
import logging
import json
import os

logger = logging.getLogger(__name__)


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    nao_rest()
    return render(request, 'activities/home.html')


def activity_finished(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    nao_rest()
    return render(request, 'activities/activity_finished.html')


def activity_failed(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    nao_rest()
    return render(request, 'activities/activity_failed.html')


def activity01(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.info("Starting activity one...")
    patients = User.objects.filter(groups__name='Patients')

    if request.method == 'POST':
        form = Activity01Form(request.POST, request.FILES)

        if form.is_valid():
            act01 = form.save(commit=False)

            act01.therapist = request.user
            act01.patient = User.objects.get(id=int(request.POST.get('patient', -1)))
            act01.answer = json.loads(request.POST.get('answer', False))
            act01.save()

            response = {'status': 1, 'success_url': reverse('activity_finished')}

        else:
            logger.error('Form has errors: {0}'.format(form.errors))
            response = {'status': 0, 'error_url': reverse('activity_failed')}

        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = Activity01Form()
        nao_wake_up()

    return render(
        request,
        'activities/activity01.html',
        {
            'form': form,
            'patients': patients,
        }
    )


def activity02(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.info("Starting activity two...")
    patients = User.objects.filter(groups__name='Patients')

    if request.method == 'POST':
        form = Activity02Form(request.POST, request.FILES)

        if form.is_valid():
            act02 = form.save(commit=False)

            act02.therapist = request.user
            act02.patient = User.objects.get(id=int(request.POST.get('patient', -1)))
            act02.answer = json.loads(request.POST.get('answer', False))
            act02.save()

            response = {'status': 1, 'success_url': reverse('activity_finished')}

        else:
            logger.error('Form has errors: {0}'.format(form.errors))
            response = {'status': 0, 'error_url': reverse('activity_failed')}

        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = Activity02Form()
        nao_wake_up()

    return render(
        request,
        'activities/activity02.html',
        {
            'form': form,
            'patients': patients,
        }
    )


def activity03(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.info("Starting activity three...")
    patients = User.objects.filter(groups__name='Patients')

    if request.method == 'POST':
        form = Activity03Form(request.POST, request.FILES)

        if form.is_valid():
            act03 = form.save(commit=False)

            act03.therapist = request.user
            act03.patient = User.objects.get(id=int(request.POST.get('patient', -1)))
            act03.answer = json.loads(request.POST.get('answer', False))
            act03.save()

            response = {'status': 1, 'success_url': reverse('activity_finished')}

        else:
            logger.error('Form has errors: {0}'.format(form.errors))
            response = {'status': 0, 'error_url': reverse('activity_failed')}

        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = Activity03Form()
        nao_wake_up()

    return render(
        request,
        'activities/activity03.html',
        {
            'form': form,
            'patients': patients,
        }
    )


def activity04(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.info("Starting activity four...")
    patients = User.objects.filter(groups__name='Patients')

    if request.method == 'POST':
        form = Activity04Form(request.POST, request.FILES)

        if form.is_valid():
            act04 = form.save(commit=False)

            act04.therapist = request.user
            act04.patient = User.objects.get(id=int(request.POST.get('patient', -1)))
            act04.answer = json.loads(request.POST.get('answer', False))
            act04.save()

            response = {'status': 1, 'success_url': reverse('activity_finished')}

        else:
            logger.error('Form has errors: {0}'.format(form.errors))
            response = {'status': 0, 'error_url': reverse('activity_failed')}

        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = Activity04Form()
        nao_wake_up()

    return render(
        request,
        'activities/activity04.html',
        {
            'form': form,
            'patients': patients,
        }
    )


def activity05(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.info("Starting activity five...")
    patients = User.objects.filter(groups__name='Patients')

    if request.method == 'POST':
        form = Activity05Form(request.POST, request.FILES)

        if form.is_valid():
            act05 = form.save(commit=False)

            act05.therapist = request.user
            act05.patient = User.objects.get(id=int(request.POST.get('patient', -1)))
            act05.answer = json.loads(request.POST.get('answer', False))
            act05.save()

            response = {'status': 1, 'success_url': reverse('activity_finished')}

        else:
            logger.error('Form has errors: {0}'.format(form.errors))
            response = {'status': 0, 'error_url': reverse('activity_failed')}

        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = Activity05Form()
        nao_wake_up()

    return render(
        request,
        'activities/activity05.html',
        {
            'form': form,
            'patients': patients,
        }
    )


def activity06(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.info("Starting activity six...")
    patients = User.objects.filter(groups__name='Patients')

    if request.method == 'POST':
        form = Activity06Form(request.POST, request.FILES)

        if form.is_valid():
            act06 = form.save(commit=False)

            act06.therapist = request.user
            act06.patient = User.objects.get(id=int(request.POST.get('patient', -1)))
            act06.answer = json.loads(request.POST.get('answer', False))
            act06.save()

            response = {'status': 1, 'success_url': reverse('activity_finished')}

        else:
            logger.error('Form has errors: {0}'.format(form.errors))
            response = {'status': 0, 'error_url': reverse('activity_failed')}

        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = Activity06Form()
        nao_wake_up()

    return render(
        request,
        'activities/activity06.html',
        {
            'form': form,
            'patients': patients,
        }
    )


def activity07(request):
    pass


def nao_speech(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    if request.method == 'GET' and request.GET.get('text') is not None:
        script = "content/scripts/nao_speech.py"
        text = request.GET.get('text')
        animation = request.GET.get('animation')
        if animation != 'none':
            script = "content/scripts/nao_animated_speech.py"

        process = subprocess.Popen([settings.PYTHON_PATH, script, text], stdout=subprocess.PIPE)
        output, error = process.communicate()

        output_lines = output.decode('UTF-8').splitlines()
        for l in output_lines:
            logger.info(l)

        data = {
            'output_lines': "Recibido!"
        }
        return JsonResponse(data)

    else:
        return HttpResponseRedirect("/")


def nao_action(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    if request.method == 'GET' and request.GET.get('action') is not None:
        python_script = "content/scripts/nao_go_to_posture.py"
        process = subprocess.Popen([settings.PYTHON_PATH, python_script, request.GET.get('action')], stdout=subprocess.PIPE)
        output, error = process.communicate()

        output_lines = output.decode('UTF-8').splitlines()
        for l in output_lines:
            logger.info(l)

        data = {
            'output_lines': "Moved!"
        }
        return JsonResponse(data)

    else:
        return HttpResponseRedirect("/")

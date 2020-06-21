"""autismws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, re_path, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from autismws import regbackend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('activities.urls')),
    path('accounts/register/', regbackend.MyRegistrationView.as_view(), name='registration_register'),
    re_path(r'^accounts/profile/(?P<pk>[\-\w]+)/$', regbackend.edit_user, name='profile'),
    path('accounts/users/', regbackend.user_list, name='user_list'),
    path('accounts/', include('registration.backends.default.urls')),
    path('login/', auth_views.login, name='login'),

    # Just to get rid of that annoying "Not found: /favicon.ico" warning
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon'),
]

from . import scheduler
import logging

logger = logging.getLogger(__name__)

# Not nice, but needed - starting the schedule to update the model
logger.info('Starting the scheduler...')
scheduler.start()

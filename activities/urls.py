from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activity01/', views.activity01, name='activity01'),
    path('activity02/', views.activity02, name='activity02'),
    path('activity03/', views.activity03, name='activity03'),
    path('activity04/', views.activity04, name='activity04'),
    path('activity05/', views.activity05, name='activity05'),
    path('activity06/', views.activity06, name='activity06'),
    path('nao_speech/', views.nao_speech, name='nao_speech'),
    path('nao_action/', views.nao_action, name='nao_action'),
    path('activity_finished/', views.activity_finished, name='activity_finished'),
    path('activity_failed/', views.activity_failed, name='activity_failed'),
]

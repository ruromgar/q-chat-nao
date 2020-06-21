from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    REG_CHOICES = (

        ('A', 'Muchas veces al día'),
        ('B', 'Unas pocas veces al día'),
        ('C', 'Unas pocas veces a la semana'),
        ('D', 'Menos de una vez al mes'),
        ('E', 'Nunca'),
    )
    WORD_CHOICES = (

        ('A', 'Muy comunes'),
        ('B', 'Más o menos comunes'),
        ('C', 'Poco comunes'),
        ('D', 'Muy infrecuentes'),
        ('E', 'Mi hijo/a no habla'),
    )
    GENDER_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    bio = models.TextField(
        max_length=1000,
        default='',
        blank=True,
        verbose_name=u'Biografía',
        help_text='Cualquier dato relevante del paciente.'
    )
    gender = models.CharField(
        max_length=1,
        default='F',
        choices=GENDER_CHOICES,
        verbose_name=u'Género'
    )
    age = models.IntegerField(
        default='12',
        verbose_name=u'Edad (en meses)'
    )
    q_ai_1 = models.CharField(
        default='A',
        max_length=1,
        choices=REG_CHOICES,
        verbose_name=u'¿Finge tu hijo/a al jugar?',
        help_text=u'Seleccionar si el niño/a es capaz de fingir mediante el juego, por ejemplo cuidar de muñecas como '
                  u'si fueran niños, hablar por un teléfono móvil de mentira....'
    )
    q_ai_2 = models.CharField(
        default='A',
        max_length=1,
        choices=REG_CHOICES,
        verbose_name=u'¿Sigue tu hijo/a la dirección de tu mirada?',
        help_text=u'Seleccionar si el niño/a suele seguir la dirección de la mirada de la persona que está con él/ella.'
    )
    q_ai_3 = models.CharField(
        default='A',
        max_length=1,
        choices=WORD_CHOICES,
        verbose_name=u'Describirías sus primeras palabras como...',
        help_text=u'Indicar la habitualidad.'
    )
    q_ai_4 = models.CharField(
        default='A',
        max_length=1,
        choices=REG_CHOICES,
        verbose_name=u'¿Suele tu hijo mirar a la nada sin propósito aparente?',
        help_text=u'Indicar si se trata de un comportamiento frecuente.'
    )
    tea = models.NullBooleanField(
        verbose_name=u'¿Presenta el paciente signos de TEA?',
        help_text=u'Este campo se completa de forma automática en función de las respuestas del usuario. Cambiar solo'
                  u' si se considera que el algoritmo está equivocado.'
    )
    added_to_dataset = models.BooleanField(
        default=False
    )


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
    post_save.connect(create_profile, sender=User)

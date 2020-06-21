from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User

from random import randint
from _datetime import datetime


class Activity01(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act01")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act01")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)
    answer = models.BooleanField(default=True)


class Activity02(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act02")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act02")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)
    answer = models.BooleanField(default=True)


class Activity03(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act03")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act03")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)
    answer = models.BooleanField(default=True)


class Activity04(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act04")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act04")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)
    answer = models.BooleanField(default=True)


class Activity05(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act05")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act05")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)
    answer = models.BooleanField(default=True)


class Activity06(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act06")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act06")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)
    answer = models.BooleanField(default=True)


class Activity07(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist_act07")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_act07")
    date = models.DateTimeField(default=datetime.now)
    comments = models.TextField(blank=True, null=True)


class Sentence(models.Model):
    sentence = models.TextField(unique=True)


class LetterValue(models.Model):
    letter = models.TextField(unique=True)
    value = models.IntegerField()
    name = models.TextField()


class SWManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class SpanishWord(models.Model):
    word = models.TextField(unique=True)
    value = models.IntegerField()

    objects = SWManager()


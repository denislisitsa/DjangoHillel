from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    subject = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()

    objects = models.Manager()


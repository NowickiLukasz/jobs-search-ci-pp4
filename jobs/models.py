from django.db import models
from django.contrib.auth.models import User
from jobs.countries import NATIONALITIES


# Create your models here.

class Profile(models.Model):
    """
        Extends User model to contain additional fields
    """
    TITLE = (
        ('mr', 'mr'),
        ('ms', 'ms'),
        ('mrs', 'mrs')
    )

    title_choices = models.CharField(max_length=10, choices=TITLE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=False)
    email = models.EmailField(max_length=256, unique=True)
    nationality = models.CharField(max_length=30, choices=NATIONALITIES)
    country_of_residence = (
            models.CharField(max_length=30, choices=NATIONALITIES)
            )
    created_on = models.DateField(auto_now=True)


# class CoverLetter(models.Model):
#     pass


# class JobListing(models.Model):
#     pass


# class SavedJob(models.Model):
#     pass


# class Employer(models.Model):
#     pass


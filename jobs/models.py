from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from jobs.countries import NATIONALITIES


# Create your models here.

# class Profile(models.Model):
#     """
#         Extends User model to contain additional fields
#     """
#     TITLE = (
#         ('mr', 'mr'),
#         ('ms', 'ms'),
#         ('mrs', 'mrs')
#     )

#     title_choices = models.CharField(max_length=10, choices=TITLE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     date_of_birth = models.DateField(null=True, blank=False)
#     email = models.EmailField(max_length=256, unique=True)
#     nationality = models.CharField(max_length=30, choices=NATIONALITIES)
#     country_of_residence = (
#             models.CharField(max_length=30, choices=NATIONALITIES)
#             )
#     created_on = models.DateField(auto_now=True)


# class CoverLetter(models.Model):
#     pass


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class JobListing(models.Model):
    """
        Creates model for details used to post and display job details.
    """
    POSITION_TYPE = (
        ('full-time', 'full-time'),
        ('part-time', 'part-time')
    )

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.PositiveSmallIntegerField()
    position_type = models.CharField(max_length=20, choices=POSITION_TYPE)
    posted_date = models.DateTimeField(auto_now=True)
    job_description = models.TextField()
    # employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + self.location 

    def get_absolute_url(self):
        return reverse('job-listing')


# class SavedJob(models.Model):
#     pass



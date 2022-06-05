from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import JobListing

# Create your views here.


# def home(request):
#     return HttpResponse("Hello World")

class Home(ListView):
    model = JobListing
    template_name = 'index.html'


class JobList(ListView):
    model = JobListing
    template_name = 'job-listing.html'

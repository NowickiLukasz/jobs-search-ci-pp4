from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    
    )
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
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


class JobDescriptionView(DetailView):
    model = JobListing
    template_name = 'job-description.html'


class AddJobView(CreateView):
    model = JobListing
    template_name = 'add-job-listing.html'
    fields = (
        'title', 'location', 'salary', 'position_type',
        'job_description',
    )


class EditJobListing(UpdateView):
    model = JobListing
    template_name = 'edit-job-listing.html'
    fields = (
        'title', 'location', 'salary', 'position_type',
        'job_description',
    )


class DeleteJobListing(DeleteView):
    model = JobListing
    template_name = 'delete-job-listing.html'
    success_url = reverse_lazy('home')



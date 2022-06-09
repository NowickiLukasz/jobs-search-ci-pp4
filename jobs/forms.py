from django import forms
from .models import JobListing


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = (
            'title', 'location', 'salary', 'position_type',
            'job_description',
        )  

    widget = {
        'title': form.TextField(attrs={'class': 'form-control'})
    }
from django.urls import path
# from . import views
from .views import (
    JobList, Home, JobDescriptionView, AddJobView, EditJobListing,
    DeleteJobListing,
)

# urlpatterns = [
#     path('', views.home, name='home')
# ]

urlpatterns = [
    # For user
    path('', Home.as_view(), name='home'),
    path('job-listing/', JobList.as_view(), name='job-listing'),
    path(
        'job-description/<int:pk>',
        JobDescriptionView.as_view(),
        name='job-description'
    ),
    path('add-job-listing/', AddJobView.as_view(), name='add-job-listing'),
    path(
        'edit-job-listing/<int:pk>',
        EditJobListing.as_view(),
        name='edit-job-listing'
    ),
    path(
        'delete-job-listing/<int:pk>',
        DeleteJobListing.as_view(),
        name='delete-job-listing'
    ),

    
]

from django.urls import path
from . import views
from .views import JobList

# urlpatterns = [
#     path('', views.home, name='home')
# ]

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('job_listing/', JobList.as_view(), name='job-listing') 
]

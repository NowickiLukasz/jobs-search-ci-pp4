from django.urls import path
# from . import views
from .views import JobList, Home

# urlpatterns = [
#     path('', views.home, name='home')
# ]

urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('job-listing/', JobList.as_view(), name='job-listing'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about_us, name='about'),
    path('contact', views.contact_us, name='contact'),
    path('job-listing/', views.job_listing, name='job-listing'),
    path('job-details/<int:pk>', views.job_details, name='job-details'),
]
from django.shortcuts import render
from job.models import Job

def home(request):
    return render(request, 'website/home.html')


def job_listing(request):
    jobs = Job.objects.filter(is_avaliable=True)
    context = {'jobs':jobs}
    return render(request, 'website/job-listing.html', context)
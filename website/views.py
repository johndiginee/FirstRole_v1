from django.shortcuts import render
from job.models import Job, ApplyJob
from .filter import Jobfilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    """Filter internships on home page."""
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_avaliable=True).order_by('-timestamp'))
    context = {'filter':filter}
    return render(request, 'website/home.html', context)


def job_listing(request):
    """List avaliable jobs/internships."""
    jobs = Job.objects.filter(is_avaliable=True).order_by('-timestamp')

    #Paginatio
    page_num = request.GET.get('page', 1)
    paginator = Paginator(jobs, 6) # 6 employees per page
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {'jobs':jobs, 'page_obj': page_obj}
    return render(request, 'website/job-listing.html', context)

def job_details(request, pk):
    """Display internship details."""
    # if ApplyJob.objects.filter(user=request.user, job=pk).exists():
    #     has_applied = True
    # else:
    #     has_applied = False
    job = Job.objects.get(pk=pk)
    context = {'job':job}
    return render(request, 'website/job_details.html', context)

def page_not_found_view(request, exception):
    return render(request, 'website/404.html', status=404)
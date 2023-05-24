import django_filters
from job.models import Job, State, Industry
from django import forms


class Jobfilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    state = django_filters.ModelChoiceFilter(
        queryset=State.objects.all(),
        empty_label="All States",
        label="States",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    industry = django_filters.ModelChoiceFilter(
        queryset=State.objects.all(),
        empty_label="All Industries",
        label="Industries",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = Job
        fields = ['title', 'state', 'job_type', 'industry']
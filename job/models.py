from django.db import models
from company.models import Company
from users.models import User

class State(models.Model):
    """Represent a State.
    
    Attributes:
        name: This is a CharField with a maximum length of 100 characters. It represents the name of the state entity.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Industry(models.Model):
    """Represent a Industry.
    
    Attributes:
        name: This is a character field that stores the name of the industry. It has a maximum length of 100 characters.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    """Represent a Job.
    
    Attributes:
        user: ForeignKey to the User class representing the user who posted the job
        company: ForeignKey to the Company class representing the company posting the job
        title: CharField representing the job title
        city: CharField representing the city where the job is located
        salary: PositiveIntegerField representing the job salary
        requirements: TextField representing the job requirements
        ideal_candidate: TextField representing the ideal candidate for the job
        is_avaliable: BooleanField representing whether the job is available or not
        timestamp: DateTimeField representing the date the job was created
        industry: ForeignKey to the Industry class representing the industry the job belongs to
        state: ForeignKey to the State class representing the state where the job is located
        job_type: CharField representing the type of job (remote, onsite, or hybrid)
    """
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=35000)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_avaliable = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    job_type = models.CharField(max_length=20, choices=job_type_choices, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.title)


class ApplyJob(models.Model):
    """Represent a ApplyJob.
    
    Attributes:
        user: ForeignKey to the User class representing the user who applied for the job
        job: ForeignKey to the Job class representing the job the user applied for
        timestamp: DateTimeField representing the date the application was created
        status: CharField representing the status of the application (accepted, declined, or pending)
    """
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices)
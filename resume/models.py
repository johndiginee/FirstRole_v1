from django.db import models
from users.models import User

class Resume(models.Model):
    """Represent a Resume.
    
    Attributes:
        user: A OneToOneField that links the resume to a user.
        first_name: A CharField to store the applicant's first name.
        surname: A CharField to store the applicant's surname.
        location: A CharField to store the applicant's location.
        job_title: A CharField to store the applicant's job title.
        upload_resume: A FileField to upload the applicant's resume/cv.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    upload_resume = models.FileField(upload_to='resume', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.surname}'
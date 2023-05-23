from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Represent a User.
    
    Attributes:
        email: a unique email address for the user
        is_recruiter: a boolean field indicating whether the user is a recruiter
        is_applicant: a boolean field indicating whether the user is an applicant
        has_resume: a boolean field indicating whether the user has a resume
        has_company: a boolean field indicating whether the user has a company.
    """
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)


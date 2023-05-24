from django.db import models
from users.models import User


class Company(models.Model):
    """Represent a Company.
    
    Attributes:
        user: A one-to-one relationship with the User class.
        name: The name of the company as a string.
        est_date: The establishment date of the company as a positive integer.
        city: The city where the company is located as a string.
        state: The state where the company is located as a string.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    est_date = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    # company_logo = models.ImageField(upload_to='logo', null=True, blank=True)
    #logo = models.ImageField(upload_to="company_logo", default="logo.jpg")

    
    # def company_logo(self):
    #     return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo.url))

    def __str__(self):
        return self.name
    
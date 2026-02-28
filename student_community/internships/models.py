from django.db import models
from companies.models import CompanyProfile

class Internship(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.TextField()
    location = models.CharField(max_length=200)
    deadline = models.DateField()
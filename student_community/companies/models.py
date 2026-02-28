from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    about = models.TextField()

    def __str__(self):
        return self.name
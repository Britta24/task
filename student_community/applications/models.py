from django.db import models
from students.models import StudentProfile
from internships.models import Internship

class Application(models.Model):

    STATUS_CHOICES = (
        ('APPLIED', 'Applied'),
        ('SHORTLISTED', 'Shortlisted'),
        ('REJECTED', 'Rejected'),
        ('SELECTED', 'Selected'),
    )

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    applied_on = models.DateTimeField(auto_now_add=True)
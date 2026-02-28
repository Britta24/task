from django.forms import ModelForm
from .models import StudentProfile

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        exclude = ['user']
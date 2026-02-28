from django.forms import ModelForm
from .models import CompanyProfile

class CompanyProfileForm(ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ['user']
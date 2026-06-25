from django import forms
from .models import SafetyReport

class SafetyReportForm(forms.ModelForm):
    class Meta:
        model=SafetyReport
        fields=['area','category','rating','description']
        
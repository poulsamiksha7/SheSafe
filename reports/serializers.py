from rest_framework import serializers
from .models import SafetyReport

class SafetyReportSearlizer(serializers.ModelSerializer):
    class Meta:
        model=SafetyReport
        fields=['id','city','locality','category','rating','description','created_at']
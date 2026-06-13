from django.db import models

# Create your models here.
class SafetyReport(models.Model):
    area=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    rating=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
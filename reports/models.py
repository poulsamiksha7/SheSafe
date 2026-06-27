from django.db import models

# Create your models here.
class SafetyReport(models.Model):
    area=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    rating=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
MAHARASHTRA_CITIES=[
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Nagpur','Nagpur'),
    ('Nashik','Nashik'),
    ('Nanded','Nanded'),
    ('Aurangabad','Aurangabad'),
    ('Other','Other'),
]
CATEGORY_CHOICES=[
    ('Street Lighting','Street Lighting'),
    ('Public Transport','Public Transport'),
    ('Late Night Safety','Late Night Safety'),
    ('Harassment Incident','Harassment Incident'),
    ('Crowded/Safe','Crowded/Safe'),
]

class SafetyReport(models.Model):
    city=models.CharField(max_length=50,choices=MAHARASHTRA_CITIES,default='Pune')
    locality=models.CharField(max_length=100,help_text='e.g. Wagholi, Kharadi, Hinjewadi')
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    rating=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.locality},{self.city}"

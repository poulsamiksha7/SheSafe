from django.shortcuts import render
from django.http import HttpResponse
from .models import SafetyReport
# Create your views here.
def home(request):
    reports=SafetyReport.objects.all()
    return render(request,'reports/home.html',{'reports':reports})
def about(request):
    return HttpResponse("Built By Samiksha Poul")
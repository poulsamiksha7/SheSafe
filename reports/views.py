from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SafetyReportForm
from django.http import HttpResponse
from .models import SafetyReport
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    reports=SafetyReport.objects.all()
    return render(request,'reports/home.html',{'reports':reports})
def about(request):
    return HttpResponse("Built by Samiksha Poul")

@login_required
def add_report(request):
    if request.method=='POST':
        form=SafetyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =SafetyReportForm()
    return render(request,'reports/add_report.html',{'form':form})
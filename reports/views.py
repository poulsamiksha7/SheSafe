from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SafetyReportForm
from django.http import HttpResponse
from .models import SafetyReport
from django.shortcuts import render, redirect
from django.db.models import Avg
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

def area_list(request):
    areas=SafetyReport.objects.values('city').annotate(avg_rating=Avg('rating')).order_by('city')
    return render(request,'reports/area_list.html',{'areas':areas})

def area_detail(request,city_name):
    reports=SafetyReport.objects.filter(city=city_name)
    avg=reports.aggregate(Avg('rating'))['rating__avg']
    return render(request,'reports/area_detail.html',{
        'city_name':city_name,
        'reports':reports,
        'avg_rating':avg,
    })
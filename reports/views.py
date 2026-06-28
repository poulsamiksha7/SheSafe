from django.contrib.auth.decorators import login_required
from .forms import SafetyReportForm
from django.http import HttpResponse
from .models import SafetyReport
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SafetyReportSearlizer

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
            report=form.save(commit=False)
            report.user=request.user
            report.save()
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

@login_required
def my_reports(request):
    reports=SafetyReport.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'reports/my_reports.html',{'reports':reports})

@login_required
def edit_report(request,report_id):
    report= get_object_or_404(SafetyReport,id=report_id,user=request.user)
    if request.method=='POST':
        form=SafetyReportForm(request.POST,instance=report)
        if form.is_valid():
            form.save()
            return redirect('my_reports')
    else:
        form=SafetyReportForm(instance=report)
    return render(request,'reports/add_report.html',{'form':form,'editing':True})

@login_required
def delete_report(request,report_id):
    report=get_object_or_404(SafetyReport,id=report_id,user=request.user)
    if request.method=='POST':
        report.delete()
        return redirect('my_reports')
    return render(request,'reports/confirm_delete.html',{'report':report})

@api_view(['GET'])
def api_reports(request):
    reports=SafetyReport.objects.all()
    serializer=SafetyReportSearlizer(reports,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_areas(request):
    areas=SafetyReport.objects.values('city').annotate(avg_rating=Avg('rating')).order_by('city')
    return Response(list(areas))

@api_view(['POST'])
def api_add_report(request):
    serializer=SafetyReportSearlizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)
 
@login_required
def delete_report(request,report_id):
    report=get_object_or_404(SafetyReport,id=report_id,user=request.user)
    if request.method=='POST':
        report.delete()
        return redirect('my_reports')
    return render(request,'reports/confirm_delete.html',{'report':report})
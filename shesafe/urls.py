"""
URL configuration for shesafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('add/', views.add_report, name='add_report'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('areas',views.area_list, name='area_list'),
    path('areas/<str:city_name>/',views.area_detail,name='area_detail'),
    path('my_reports/',views.my_reports,name='my_reports'),
    path('edit/<int:report_id>/',views.edit_report,name='edit_report'),
    path('delete/<int:report_id>',views.delete_report,name='delete_report'),
    path('api/reports/',views.api_reports,name='api_reports'),
    path('api/areas/',views.api_areas,name='api_areas'),
    path('api/reports/add/',views.api_add_report,name='api_add_report'),

]

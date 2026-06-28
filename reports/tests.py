from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from .models import SafetyReport

# Create your tests here.

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser',password='testpass123')

@pytest.fixture
def report(db,user):
    return SafetyReport.objects.create(
        user=user,city='Pune',locality='Wagholi',
        category='Street Lighting', rating=3, description='Test report'
    )

def test_add_report_requires_login(client):
    response=client.get('/add/')
    assert response.status_code==302 

def test_logged_in_user_can_access_add_report(client,user):
    client.login(username='testuser',password='testpass123')
    response=client.get('/add/')
    assert response.status_code==200

def test_report_creation(report):
    assert report.city=='Pune'
    assert report.rating==3

def test_average_rating_calculation(db,user):
    SafetyReport.objects.create(user=user, city='Kharadi',locality='X',category='Public Transport', rating=4, description='a')
    SafetyReport.objects.create(user=user,city='Kharadi',locality='Y', category='Public Transport', rating=2, description='b')
    from django.db.models import Avg
    avg=SafetyReport.objects.filter(city='Kharadi').aggregate(Avg('rating'))['rating__avg']
    assert avg==3.0

def test_user_cannot_delete_others_report(client,report):
    other_user=User.objects.create_user(username='other', password='pass123')
    client.login(username='other',password='pass123')
    response=client.get(f'delete/{report.id}/')
    assert response.status_code==404

def test_user_cannot_delete_others_report(client,report):
    other_user=User.objects.create_user(username='other',password='pass123')
    client.login(username='other',password='pass123')
    response=client.get(f'/delete/{report.id}/')
    assert response.status_code==404

def test_user_can_delete_own_report(client,user,report):
    client.login(username='testuser',password='testpass123')
    print(f'Report ID: {report.id}, Report user: {report.user}, Test user: {user}')
    response=client.post(f'/delete/{report.id}/')
    assert response.status_code==302
    assert not SafetyReport.objects.filter(id=report.id).exists()



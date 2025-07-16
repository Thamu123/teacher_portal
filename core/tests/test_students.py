import pytest
from core.models import Student
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_new_student(api_client):
    response = api_client.post('/api/students/', {
        "name": "Varun",
        "subject": "Math",
        "marks": 90
    })
    assert response.status_code == 201
    student = Student.objects.get(name="Varun", subject="Math")
    assert student.marks == 90

@pytest.mark.django_db
def test_create_duplicate_student_adds_marks(api_client):
    Student.objects.create(name="Bala", subject="Science", marks=40)
    response = api_client.post('/api/students/', {
        "name": "Bala",
        "subject": "Science",
        "marks": 20
    })
    assert response.status_code == 201
    student = Student.objects.get(name="Bala", subject="Science")
    print(student.marks)
    assert student.marks == 60

@pytest.mark.django_db
def test_update_student(api_client):
    student = Student.objects.create(name="Deva", subject="Biology", marks=70)
    response = api_client.put(f'/api/students/{student.id}/', {
        "name": "Deva",
        "subject": "Biology",
        "marks": 75
    }, content_type='application/json')
    assert response.status_code == 200
    updated = Student.objects.get(id=student.id)
    assert updated.name == "Deva"
    assert updated.marks == 75

@pytest.mark.django_db
def test_delete_student(api_client):
    student = Student.objects.create(name="Dave", subject="History", marks=50)
    response = api_client.delete(f'/api/students/{student.id}/')
    assert response.status_code == 204
    assert not Student.objects.filter(id=student.id).exists()

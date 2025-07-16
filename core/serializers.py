from rest_framework import serializers
from django.db import transaction
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'subject', 'marks')

    @transaction.atomic()
    def create(self, validated_data):
        name = validated_data['name']
        subject = validated_data['subject']
        marks = validated_data.get('marks', 0)
        student = Student.objects.filter(name__iexact=name, subject__iexact=subject).first()
        if student:
            student.marks += marks
            student.save()
            return student
        else:
            student = Student.objects.create(name=name, subject=subject, marks=marks)
        return student

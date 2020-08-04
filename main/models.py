from django.db import models
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


class Coures(models.Model):
    cou_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    teacher_name = models.CharField(max_length=50)
    date = models.DateField()

    def empty_view(self):
        consta = {'Available': 'Unavailable'}
        return Response(consta, status=status.HTTP_404_NOT_FOUND)

class Student(models.Model):
    student_id = models.IntegerField()
    coures = models.ForeignKey(Coures, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    parent = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



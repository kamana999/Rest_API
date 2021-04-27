from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)
    address = models.TextField()
    dob = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class College(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=50)
    address = models.TextField()
    doc = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.college_name

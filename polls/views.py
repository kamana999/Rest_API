from django.shortcuts import render,get_object_or_404
from .models import Student, College
from django.http import Http404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from .searilizers import *


def index(request):
    student = Student.objects.all()
    return render(request, 'index.html', {'students':student})


def detail(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student Does not exist")
    college = College.objects.filter(id=id)
    return render(request, 'detail.html', {
        'students':student,
        'colleges':college,
    })


class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny, ]


class StudentSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [AllowAny, ]


class CollegeSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class =  CollegeSerializers
    permission_classes = [IsAuthenticated, ]
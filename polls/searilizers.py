from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'address', 'contact', 'dob']


class CollegeSerializers(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['student', 'college_name', 'address', 'doc']



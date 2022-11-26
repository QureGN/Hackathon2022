from notes.models import Years, Departments, Users, Subjects, Notes, Sub_Notes
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend


class YearsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Years
        # Поля, которые мы сериализуем
        fields = ["pk", "Count"]


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Departments
        # Поля, которые мы сериализуем
        fields = ["pk", "DepName"]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["pk", "Login", "Password", "Dep", "Year"]


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ["pk", "SubName", "Dep", "Year"]


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["pk", "Type", "User", "Deadline", "Personal_Deadline", "Passed", "Text"]


class Sub_NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Notes
        fields = ["pk", "Notes", "User", "Sub"]



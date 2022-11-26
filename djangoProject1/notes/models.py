from django.db import models
from django_filters import rest_framework as filters


class Years(models.Model):
    Count = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'Years'

class Departments(models.Model):
    DepName = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'Departments'


class Users(models.Model):
    Login = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    Dep = models.ForeignKey(Departments, on_delete=models.CASCADE)
    Year = models.ForeignKey(Years, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'Users'
class Subjects(models.Model):
    SubName = models.CharField(max_length=50)
    Dep = models.ForeignKey(Departments, on_delete=models.CASCADE)
    Year = models.ForeignKey(Years, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'Subjects'

class Notes(models.Model):
    Type = models.CharField(max_length=25)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Deadline = models.DateField()
    Personal_Deadline = models.DateField()
    Passed = models.BooleanField()
    Text = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'Notes'

class Sub_Notes(models.Model):
    Notes = models.ForeignKey(Notes, on_delete=models.CASCADE)
    Sub = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'Sub_Notes'


class CharFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class SubjectFilter(filters.FilterSet):
    Dep = CharFilterInFilter(field_name ='Dep', lookup_expr ='in')

    Year = CharFilterInFilter(field_name ='Year', lookup_expr ='in')

    class Meta:
        model: Subjects
        fields = ['Dep', 'Year']

class NoteFilter(filters.FilterSet):
    User = CharFilterInFilter(field_name ='User', lookup_expr ='in')


    class Meta:
        model: Users
        fields = ['User']


# Create your models here.

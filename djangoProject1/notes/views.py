from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from notes.serializers import UsersSerializer,SubjectsSerializer, DepartmentsSerializer, YearsSerializer, NotesSerializer, Sub_NotesSerializer
from notes.models import Users, Subjects, Departments, Years, Sub_Notes, Notes, SubjectFilter, NoteFilter
from django_filters.rest_framework import DjangoFilterBackend

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Users.objects.all().order_by('pk')
    serializer_class = UsersSerializer

class SubjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Subjects.objects.all().order_by('pk')
    serializer_class = SubjectsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SubjectFilter


class DepartmentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Departments.objects.all().order_by('pk')
    serializer_class = DepartmentsSerializer


class NotesViewSet(viewsets.ModelViewSet):
        """
        API endpoint, который позволяет просматривать и редактировать акции компаний
        """
        # queryset всех пользователей для фильтрации по дате последнего изменения

        queryset = Notes.objects.all().order_by('pk')
        serializer_class = NotesSerializer
        filter_backends = (DjangoFilterBackend,)
        filterset_class = NoteFilter


class Sub_NotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Sub_Notes.objects.all().order_by('pk')
    serializer_class = Sub_NotesSerializer

class YearsViewSet(viewsets.ModelViewSet):
        """
        API endpoint, который позволяет просматривать и редактировать акции компаний
        """
        # queryset всех пользователей для фильтрации по дате последнего изменения
        queryset = Years.objects.all().order_by('pk')
        serializer_class = YearsSerializer

# Create your views here.
# Create your views here.

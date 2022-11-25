from django.contrib import admin
from .models import Users, Notes, Subjects, Sub_Notes, Years, Departments

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'Login', 'Password')
    list_display_links = ('id', 'Login', 'Password')
admin.site.register(Users, UsersAdmin)

class YearsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Count')
    list_display_links = ('id', 'Count')
admin.site.register(Years, YearsAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'DepName')
    list_display_links = ('id', 'DepName')
admin.site.register(Departments, DepartmentsAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'SubName' )
    list_display_links = ('id', 'SubName')
admin.site.register(Subjects, SubjectsAdmin)

class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Type', 'Deadline', 'Personal_Deadline', 'Passed', 'Text' )
    list_display_links = ('id', 'Type',  'Deadline', 'Personal_Deadline', 'Passed', 'Text' )
admin.site.register(Notes, NotesAdmin)


# Register your models here.

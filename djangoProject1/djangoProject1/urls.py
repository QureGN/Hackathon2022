"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notes import views as stock_views

router = routers.DefaultRouter()
router.register(r'Years', stock_views.YearsViewSet)
router.register(r'Users', stock_views.UsersViewSet)
router.register(r'Subjects', stock_views.SubjectsViewSet)
router.register(r'Departments', stock_views.DepartmentsViewSet)
router.register(r'Notes', stock_views.NotesViewSet)
router.register(r'Sub_Notes', stock_views.Sub_NotesViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
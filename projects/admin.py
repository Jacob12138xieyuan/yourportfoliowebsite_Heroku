from django.contrib import admin
from .models import Project, UserProfile
# Register your models here.


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'summary', 'submission_date']


@admin.register(UserProfile)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['user', 'profileImage', 'fullName', 'profileSummary']

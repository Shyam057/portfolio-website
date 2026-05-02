from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'is_featured', 'order']
    list_filter = ['is_featured']
    ordering = ['order']
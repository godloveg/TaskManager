from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'usetr', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'usetr__username')
    ordering = ('-created_at',)


from django.contrib import admin
from App.models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'content','created_at','updated_at']
    list_display_links = ['id', 'header', 'content','created_at','updated_at']
    
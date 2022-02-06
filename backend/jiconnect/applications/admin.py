from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'app_type', 'location')
    list_display_links = ('id', 'customer')
    search_field = ('customer')
    list_per_page = 5

admin.site.register(Application, ApplicationAdmin)

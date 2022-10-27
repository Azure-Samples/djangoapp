from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)

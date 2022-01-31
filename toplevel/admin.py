from django.contrib import admin

from .models import Resource, Service

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_of_resource',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Resource, ResourceAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)

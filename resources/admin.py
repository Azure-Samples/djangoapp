from django.contrib import admin
from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_of_resource')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Resource, ResourceAdmin)

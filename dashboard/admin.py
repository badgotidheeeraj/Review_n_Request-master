from django.contrib import admin
from .models import RequestModule, MasterModule, Resource, ReviewModule
from core.models import UserAccount

# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "request_name", "ModuleName", "json_field", "created_at", "is_favorite"
                    ]

class MasterModuleAdmin(admin.ModelAdmin):
    list_display = ["id", 'module_name',
                    'json_field']

class ReviewModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'review_name',
                    'request_name', 'json_field', 'review_type', 'is_favorite']

class ResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'json_field']

admin.site.register(RequestModule, ModuleAdmin)
admin.site.register(ReviewModule,ReviewModuleAdmin)

'''
WARNING!!! 
DO NOT UNCOMMENT BELOW (nhi touch kr rha, jalwa hai tumhara) 
'''
# admin.site.register(Resource, ResourceAdmin)
admin.site.register(MasterModule, MasterModuleAdmin)

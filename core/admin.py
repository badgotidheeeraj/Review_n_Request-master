from django.contrib import admin
from .models import UserAccount, UserProfile
from django.utils.translation import gettext_lazy as _

# Register your models here.

# class UserAccountAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username','full_name','email', 'is_expert', 'is_active', 'is_staff')

#     fieldsets = (
#         (None, {"fields": ('username','password')}),
#         (_('Personal info'),{'fields':('full_name','email')}),
#         (_('Permissions'),{'fields':('is_active', 'is_expert' , 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )

#####################################################################


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'email',
                    'is_expert', 'is_active', 'is_staff')

    fieldsets = (
        (None, {"fields": ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_expert',
         'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


#####################################################################

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'userAccount', 'area', 'domain','whatsApp_no','country','state')

    fieldsets = (
        (_('Profile info'), {"fields": ('userAccount','about')}),
        (_('Contact info'),{'fields':('whatsApp_no','phone_no','phone_same_as_whatsapp')}),
        (_('Professional info'),{'fields':('area', 'domain')}),
        (_('Verification info'),{'fields':('email_is_verified','phone_is_verified','whatsApp_no_is_verified')}),
        (_('Address info'),{'fields':('country','state','city','address')}),
    )
    

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
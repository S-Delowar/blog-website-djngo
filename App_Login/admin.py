from django.contrib import admin
from App_Login.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',  'profile_pic']

admin.site.register(UserProfile, UserProfileAdmin)
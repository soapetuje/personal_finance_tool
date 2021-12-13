from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin


from .models import User, Profile, Price

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')

admin.site.register(User, UserAdmin)

admin.site.register(Profile)

admin.site.register(Price)


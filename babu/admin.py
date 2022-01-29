from django.contrib import admin
from .models import student

# Register your models here.


# @admin.register(student)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email', 'password')
admin.site.register(student)

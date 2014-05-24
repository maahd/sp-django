from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import *


# Register your models here.

class DoctorSeekerAdmin(admin.ModelAdmin):
    pass
admin.site.register(DoctorSeeker, DoctorSeekerAdmin)


class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)


class SpecializationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Specialization, SpecializationAdmin)


class ClinicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clinic, ClinicAdmin)
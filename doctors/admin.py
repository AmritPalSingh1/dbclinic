from django.contrib import admin

from .models import Doctor, Schedule, Appointment

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Schedule)

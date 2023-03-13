from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'customer', 'status')
    actions = ['approve_selected']

    def approve_selected(self, request, queryset):
        for appointment in queryset:
            appointment.approve()
        self.message_user(request, 'Selected appointments have been approved.')
    approve_selected.short_description = 'Approve selected appointments'

admin.site.register(Appointment, AppointmentAdmin)

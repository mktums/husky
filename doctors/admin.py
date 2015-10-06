from django.contrib import admin
from .models import Record, Doctor


class RecordInline(admin.TabularInline):
    model = Record
    extra = 0
    ordering = ('date', 'time')
    max_num = 50


class DoctorAdmin(admin.ModelAdmin):
    inlines = [RecordInline, ]


class RecordAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time')
    date_hierarchy = 'date'
    list_filter = ('doctor', 'date', 'time')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Record, RecordAdmin)

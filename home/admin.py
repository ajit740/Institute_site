from django.contrib import admin
from .models import Notice, Testimonial

admin.site.register(Notice)
admin.site.register(Testimonial)

from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'submitted_at')

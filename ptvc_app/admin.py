from django.contrib import admin
from ptvc_app.models import Contact, Subject, Day, Employee

# Register your models here.
admin.site.register(Subject)
admin.site.register(Contact)
admin.site.register(Day)
admin.site.register(Employee)

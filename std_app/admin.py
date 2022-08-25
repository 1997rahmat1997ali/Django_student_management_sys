from django.contrib import admin
from .models import Student, Sec, Department
# Register your models here.

admin.site.register(Student)
admin.site.register(Sec)
admin.site.register(Department)
from django.contrib import admin

# Register your models here.
from .models import Student, Cursus

admin.site.register(Student)
admin.site.register(Cursus)
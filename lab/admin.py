from django.contrib import admin
from .models import Person,Doctor,Test

admin.site.register(Person)
admin.site.register(Doctor)
admin.site.register(Test)

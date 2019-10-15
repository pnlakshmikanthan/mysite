from django.contrib import admin
from lab.models import Person,Doctor,Test

class TestAdmin(admin.ModelAdmin):
    list_display = ['id','test_name', 'test_result', 'test_normalvalue']

admin.site.register(Test,TestAdmin)
admin.site.register(Person)
admin.site.register(Doctor)


from django.contrib import admin

# Register your models here.
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=['Sr_No','Division','RollNo','Name','Accountancy','English','Maths','Economics','Business_Studies','Total','Average','Grade','Result']

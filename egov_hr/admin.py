from django.contrib import admin
from egov_hr.models import *





class EmployeeAdmin(admin.ModelAdmin):
   # fields = ('employee_ref','title', 'first_name','middle_name', 'last_name','gender','date_of_birth', 'ministry_or_angency', 'date_hire','department_name','image','address','city', 'county','email','mobile')
    list_display = ['employee_ref', 'first_name','middle_name', 'last_name','gender', 'ministry_or_angency','department_name', 'county']
admin.site.register(Employee,EmployeeAdmin)

admin.site.register(MinistryAgency)
admin.site.register(Contract)

admin.site.register(Department)

class JobAdmin(admin.ModelAdmin):
    list_display = ['job_ref', 'title']

admin.site.register(Job, JobAdmin)

class JobHistoryAdmin(admin.ModelAdmin):
    list_display = ['job', 'employee', 'start_date', 'end_date']

admin.site.register(JobHistory, JobHistoryAdmin)

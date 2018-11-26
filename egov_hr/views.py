from django.shortcuts import render


def index(request):
    return render(request, 'egov_hr/hr-dashboard.html')

def newemployee(request):
    return render(request, 'egov_hr/new-employee.html')

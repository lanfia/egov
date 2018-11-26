from django.contrib import admin

from egov_emr.models import *

admin.site.register(Country)
admin.site.register(HealthCenter)
admin.site.register(Allergy)
admin.site.register(Reaction)
admin.site.register(NextOfKin)
admin.site.register(PatienceRecord)
admin.site.register(PatienceAllegy)
admin.site.register(DiagnosticCategory)
admin.site.register(Diagnostic)
admin.site.register(Visit)
admin.site.register(DiagnosticResult)

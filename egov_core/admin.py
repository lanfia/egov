from django.contrib import admin
from .models import Profile, Partner


admin.site.site_header = 'eGov Liberia'
admin.site.site_title = "eGov Liberia Admin Portal"
admin.site.index_title = "Welcome to EGOV Liberia"

admin.site.register(Profile)
admin.site.register(Partner)

from django.contrib import admin
from django.urls import path, include
from egov_core import urls



urlpatterns = [
     path('jet/', include('jet.urls', 'jet')),
     path('', admin.site.urls),
   # path('', include('egov_core.urls')),
  #  path('hr/', include('egov_hr.urls')),

    
]

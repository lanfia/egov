
from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='hr-dashboard'),
    path('newemployee/', views.newemployee, name='newemployee'),
    path('admin/', admin.site.urls),
    
]

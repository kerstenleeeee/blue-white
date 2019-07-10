from django.urls import path
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bts/', views.bts, name="btsView"),
    path('ue/', views.ue, name="ueView"),
    path('medi/a', views.racks, name="mediaview"),
    path('exportBTSPC', views.exportCSV_BTSPC, name='exportCSV_BTSPC'),
    path('exportBTSINFO', views.exportCSV_BTSINFO, name='exportCSV_BTSINFO'),
    path('exportBTSMOD', views.exportCSV_BTSMOD, name='exportCSV_BTSMOD'),
    path('exportTMPC', views.exportCSV_TMPC, name='exportCSV_TMPC'),
    path('exportTMINFO', views.exportCSV_TMINFO, name='exportCSV_TMINFO'),
    path('/download/<str:file_name>/', views.download),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bts/', views.bts, name="btsView"),
    path('ue/', views.ue, name="ueView"),
    path('racks/', views.racks, name="rackView"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
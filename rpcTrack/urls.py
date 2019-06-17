from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bts/', views.bts, name="btsView"),
    path('ue/', views.ue, name="ueView"),
]
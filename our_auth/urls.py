from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('starting/',views.starting, name="starting"),
    path('autheticate/',views.finding,name="authenticating"),
    path('registering/',views.registering,name="registering"),
]

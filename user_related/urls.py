from django.urls import path
from . import views

urlpatterns = [
    # GOTTA CONTINUE
    path('user/<str:tab_name>/<str:tkn>/', views.load_tab, name="load_tab"),
]

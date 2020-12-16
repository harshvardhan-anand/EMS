from django.urls import path
from . import views

app_name = 'show_admin'

urlpatterns = [
    path('', views.admin, name='admin'),
    path('action', views.operation, name='operation'),
    path('result', views.result, name='result')
]
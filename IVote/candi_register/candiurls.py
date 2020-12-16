from django.urls import path
from . import views

app_name = 'candi_register'

urlpatterns = [
    path('', views.candidate_register, name='register')
]
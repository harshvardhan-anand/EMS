from django.urls import path
from . import views
app_name = 'info'

urlpatterns = [
    path('', views.show_candidate, name='showcandidate')
]
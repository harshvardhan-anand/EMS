from django.urls import path
from . import views

app_name = 'voter'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('vote', views.vote, name='vote'),
    path('voted', views.voted, name='voted')
]
from django.urls import path
from . import views

app_name = 'home_pag'

urlpatterns = [
    path('', views.home, name='home'),
]
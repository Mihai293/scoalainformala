from userprofile import views
from django.urls import path

app_name = 'userprofile'

urlpatterns = [
    path('new_acount/', views.CreateNewAccount.as_view(), name='utilizator_nou'),
    path('start_timesheet/', views.new_timesheet, name='start_pontaj'),
    path('stop_timesheet/', views.stop_timesheet, name='oprire_pontaj'),


]
from userprofile import views
from django.urls import path

app_name = 'userprofile'

urlpatterns = [
    path('new_acount/', views.CreateNewAccount.as_view(), name='utilizator_nou')
]
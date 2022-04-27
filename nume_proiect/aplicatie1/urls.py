from django.urls import path

from aplicatie1 import views

app_name = 'location'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='lista_locati'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_location, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),
    path('locati_inactive', views.LocationInactiveView.as_view(), name='locati_inactive'),
]
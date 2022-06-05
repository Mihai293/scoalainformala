from django.urls import path
from coinmarket_api import views

app_name = 'crypto'

urlpatterns = [
    path('', views.coin, name='coin'),
    path('listare/', views.WalletView.as_view(), name='listare'),
    path('add/', views.WalletCreate.as_view(), name='add'),
    path('<int:pk>/update/', views.Edit_coin.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.del_coin, name='sterge'),



]
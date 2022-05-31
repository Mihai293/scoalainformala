from django.urls import path
from coinmarket_api import views

app_name = 'crypto'

urlpatterns = [
    path('', views.coin, name='coin'),
    path('add/', views.WalletCreate.as_view(), name='add'),
    path('', views.WalletView.as_view(), name='listare'),

]
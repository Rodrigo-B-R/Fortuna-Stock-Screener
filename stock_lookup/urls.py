from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name= 'home'),
    path('stock_overview', views.stock_view, name= 'stock_view')

    
]
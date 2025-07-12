from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name= 'home'),
    path('stock_overview', views.stock_view, name= 'stock_view'),
    path('error',views.error_view,name='error')

    
]
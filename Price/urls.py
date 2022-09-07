from django.urls import path , include
from .views import ChartCreate , fcreate

urlpatterns = [
    
    path('',ChartCreate.as_view() , name ='priceshow'),
    path('display',fcreate , name ='display'),
]

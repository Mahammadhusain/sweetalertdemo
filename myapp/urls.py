from django.urls import path
from .views import ProductAdd,Productdelete
urlpatterns = [
    path('',ProductAdd,name='add'),
    path('del/<int:id>/',Productdelete,name='delete'),
]

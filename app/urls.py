from django.urls import path,include
from . import views




urlpatterns = [
    path('closest', views.c_point,name='c_point'),
]
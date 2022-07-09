from . import views
from django.urls import path

urlpatterns = [
    path('home', views.home_page),
    path('home/<int:pk>',views.get_item)
]

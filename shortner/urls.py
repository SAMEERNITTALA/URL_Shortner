from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:shortened_url>/', views.redirect_url, name='redirect_url'),
]

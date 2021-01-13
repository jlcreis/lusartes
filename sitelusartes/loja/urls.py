from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.LojaIndex, name='index'),
    path('produtos/', views.LojaProdutos, name='produtos'),
]
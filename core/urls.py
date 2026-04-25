from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.add_card, name='add_card'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
    path('calculate/', views.calculate, name='calculate'),
]
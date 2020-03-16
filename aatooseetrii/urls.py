from django.urls import path
from . import views

urlpatterns = [
    path('', views.Startaatooseetrii, name='home'),
    path('raportti', views.Raportti.as_view(), name='raportti'),
    path('api/', views.ListNatPark.as_view()),
    path('api/<int:pk>/', views.DetailNatPark.as_view()),
]
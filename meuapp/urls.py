from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Mapeia a URL raiz para a view index
]


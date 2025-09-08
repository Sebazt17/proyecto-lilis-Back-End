from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('subcatalogo/<str:categoria>/', views.subcatalogo, name='subcatalogo'),
    path('detalle/<str:producto>/', views.detalle_producto, name='detalle_producto'),
]
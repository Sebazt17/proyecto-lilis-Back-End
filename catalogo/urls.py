from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empresa/', views.empresa, name='empresa'),
    path('categoria/<str:categoria>/',views.subcatalogo, name='subcatalogo'),
    path('producto/<str:producto>/', views.detalle_producto, name='detalle_producto'),
]

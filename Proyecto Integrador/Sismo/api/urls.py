from django.urls import path
from . import views

urlpatterns = [
    path('empresa/',views.EmpresaView.as_view()),
    path('empresa/<int:empresa_id>',views.EmpresaDetailView.as_view()),
    path('intensidad/',views.IntensidadView.as_view()),
    path('intensidad/<int:intensidad_id>',views.IntensidadDetailView.as_view()),
    path('sensor/',views.SensorView.as_view()),
    path('sensor/<int:sensor_id>',views.SensorDetailView.as_view()),
    path('usuario/',views.UsuarioView.as_view()),
    path('usuario/<int:usuario_id>',views.UsuarioDetailView.as_view()),
    path('zona/',views.ZonaView.as_view()),
    path('zona/<int:zona_id>',views.ZonaDetailView.as_view()),
    
]
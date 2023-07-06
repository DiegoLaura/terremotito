from rest_framework import generics
from terremotito.models import Empresa, Intensidad, Sensor, Usuario, Zona
from .serializers import EmpresaSerializer, IntensidadSerializer, SensorSerializer, UsuarioSerializer, ZonaSerializer


class EmpresaView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    lookup_url_kwarg = 'empresa_id'
    serializer_class = EmpresaSerializer



class IntensidadView(generics.ListCreateAPIView):
    queryset = Intensidad.objects.all()
    serializer_class = IntensidadSerializer

class IntensidadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intensidad.objects.all()
    lookup_url_kwarg = 'intensidad_id'
    serializer_class = IntensidadSerializer



class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    lookup_url_kwarg = 'sensor_id'
    serializer_class = SensorSerializer



class UsuarioView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    lookup_url_kwarg = 'usuario_id'
    serializer_class = UsuarioSerializer



class ZonaView(generics.ListCreateAPIView):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer

class ZonaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zona.objects.all()
    lookup_url_kwarg = 'zona_id'
    serializer_class = ZonaSerializer

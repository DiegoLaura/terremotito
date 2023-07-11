from django.test import TestCase, Client
from .models import Empresa, Intensidad, Zona, Sensor, Usuario
from django.urls import reverse
from .models import Empresa, Intensidad, Zona, Sensor, Usuario
from random import randrange

class EmpresaModelTestCase(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(nombre='Mi Empresa', telefono='123456789')

    def test_str_representation(self):
        self.assertEqual(str(self.empresa), 'Mi Empresa')

class IntensidadModelTestCase(TestCase):
    def setUp(self):
        self.intensidad = Intensidad.objects.create(tiempo='2023-07-09 12:00:00', movimiento=1)

    def test_str_representation(self):
        expected_str = 'Tiempo 2023-07-09 12:00:00 - Movimiento: 1'
        self.assertEqual(str(self.intensidad), expected_str)

class ZonaModelTestCase(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(nombre='Mi Empresa', telefono='123456789')
        self.zona = Zona.objects.create(nombre='Zona 1', empresa=self.empresa)

    def test_str_representation(self):
        self.assertEqual(str(self.zona), 'Zona 1')

class SensorModelTestCase(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(nombre='Mi Empresa', telefono='123456789')
        self.zona = Zona.objects.create(nombre='Zona 1', empresa=self.empresa)
        self.sensor = Sensor.objects.create(nombre='Sensor 1', zona=self.zona, empresa=self.empresa)

    def test_str_representation(self):
        self.assertEqual(str(self.sensor), 'Sensor 1')

class UsuarioModelTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(usuario='john_doe', correo='john@example.com', clave='password')

    def test_str_representation(self):
        self.assertEqual(str(self.usuario), 'john_doe')
        
class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.empresa = Empresa.objects.create(nombre='Mi Empresa', telefono='123456789')
        self.zona = Zona.objects.create(nombre='Zona 1', empresa=self.empresa)
        self.usuario = Usuario.objects.create(usuario='john_doe', correo='john@example.com', clave='password')

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_chart_view(self):
        url = reverse('get_chart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        chart_data = response.json()
        self.assertIn('xAxis', chart_data)
        self.assertIn('yAxis', chart_data)
        self.assertIn('series', chart_data)

    def test_sismo_view(self):
        url = reverse('sismo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sismo.html')
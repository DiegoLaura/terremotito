from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Empresa),
admin.site.register(Intensidad),
admin.site.register(Sensor),
admin.site.register(Usuario),
admin.site.register(Zona),
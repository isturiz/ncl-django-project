from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece la configuración de Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usa la configuración de Django para Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga las tareas de la aplicación Django
app.autodiscover_tasks()

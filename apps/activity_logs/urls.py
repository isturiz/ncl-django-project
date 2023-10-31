from django.urls import path

from .views import auditlog_view


urlpatterns = [
    path('', auditlog_view, name='auditlog'),
]
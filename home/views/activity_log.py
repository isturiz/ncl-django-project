from django.shortcuts import render
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
import json
from django.utils.translation import gettext as _
from django.utils.translation import get_language

def action_history_view(request):
    log_entries = LogEntry.objects.all().select_related('user').order_by('-action_time')
    return render(request, 'home/action_history.html', {'log_entries': log_entries})

from django.shortcuts import render
from auditlog.models import LogEntry
from django.apps import apps
from django.utils import timezone


def get_verbose_name(model, field_name):
    # Obtén el campo a partir del nombre del campo y el modelo
    field = model._meta.get_field(field_name)

    # Obtén el nombre descriptivo traducido del campo
    verbose_name = field.verbose_name

    return verbose_name

def format_date(date_string):
    # Convierte la cadena de fecha a un objeto de fecha y hora
    try:
        date = timezone.make_aware(timezone.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
        formatted_date = date.strftime("%d/%m/%Y %H:%M:%S")
    except ValueError:
        # Si la conversión falla, asumimos que no hay hora
        date = timezone.make_aware(timezone.datetime.strptime(date_string, "%Y-%m-%d"))
        formatted_date = date.strftime("%d/%m/%Y")

    return formatted_date



def auditlog_view(request):
    log_entries = LogEntry.objects.all().order_by('-timestamp')  # Obtén las últimas 10 entradas de registro de auditoría

    for entry in log_entries:
        try:
            changes = json.loads(entry.changes)
            formatted_changes = {}
            model = entry.content_type.model_class()  # Obtén el modelo directamente

            # Translate the field names
            for field, values in changes.items():
                translated_field = get_verbose_name(model, field)
                if field == "date" or field == "birthdate":  # Reemplaza "fecha" con el nombre de tu campo de fecha
                    formatted_date = f"{format_date(values[0])} → {format_date(values[1])}"
                    formatted_changes[translated_field] = formatted_date
                else:
                    print(field)
                    formatted_changes[translated_field] = f"{values[0]} → {values[1]}"
            entry.formatted_changes = formatted_changes

            # Translate the model name
            for entry in log_entries:
                entry.model_name = _(entry.content_type.model)  # Traduce el nombre del modelo


        except json.JSONDecodeError:
            entry.formatted_changes = entry.changes


    return render(request, 'home/auditlog.html', {'log_entries': log_entries})
from django.shortcuts import render
import json
from django.utils.translation import gettext as _

from auditlog.models import LogEntry
from django.utils import timezone
from django.db import models


def get_verbose_name(model, field_name):
    # Obtén el campo a partir del nombre del campo y el modelo
    field = model._meta.get_field(field_name)

    # Verifica si el campo es una relación inversa de clave externa
    if isinstance(field, models.ManyToOneRel):
        # Accede al campo de clave externa
        related_field = field.field

        # Obtén el nombre descriptivo traducido del campo de clave externa
        verbose_name = related_field.verbose_name
    else:
        # El campo no es una relación inversa, obtén su nombre descriptivo traducido
        verbose_name = field.verbose_name

    return verbose_name

    return verbose_name

def format_date(date_string):
    if date_string is None or date_string == 'None':
        return "[Sin valor]"
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
    log_entries = LogEntry.objects.all().order_by('-timestamp')[0:10]

    DATE_FIELDS = ["date", "birthdate", "start_date", "end_date"]

    for entry in log_entries:
        try:
            changes = json.loads(entry.changes)
            formatted_changes = {}
            model = entry.content_type.model_class()  # Obtén el modelo directamente

            # Translate the field names
            for field, values in changes.items():
                
                    
                translated_field = get_verbose_name(model, field)
                if field in DATE_FIELDS:  # Reemplaza "fecha" con el nombre de tu campo de fecha
                    formatted_date = f"{format_date(values[0])} → {format_date(values[1])}"
                    if values[0] is None or values[0] == 'None' or values[0] == '':
                        values[0] = "[Sin valor]"
                    if values[1] is None or values[1] == 'None' or values[1] == '':
                        values[1] = "[Sin valor]"

                    # if values[0] == True or values[0] == 'True':
                    #     values[0] = "Sí"
                    #     print('field: ', field, 'values: ', values)
                    # if values[1] == False or values[1] == 'False':
                    #     values[1] = "No"
                    #     print('field: ', field, 'values: ', values)
                    formatted_changes[translated_field] = formatted_date
                    
                else:
                    if values[0] is None or values[0] == 'None' or values[0] == '':
                        values[0] = "[Sin valor]"
                    if values[1] is None or values[1] == 'None' or values[1] == '':
                        values[1] = "[Sin valor]"

                    # if values[0] == True or values[0] == 'True':
                    #     values[0] = "Sí"
                    #     print('field: ', field, 'values: ', values)
                    # if values[1] == False or values[1] == 'False':
                    #     values[1] = "No"
                    #     print('field: ', field, 'values: ', values)
                    formatted_changes[translated_field] = f"{values[0]} → {values[1]}"
                    

            entry.formatted_changes = formatted_changes
            

            # Translate the model name
            for entry in log_entries:
                entry.model_name = _(entry.content_type.model)  # Traduce el nombre del modelo


        except json.JSONDecodeError:
            entry.formatted_changes = entry.changes


    return render(request, 'home/auditlog.html', {'log_entries': log_entries})
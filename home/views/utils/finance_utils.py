from home.models import Payment

from datetime import datetime

import json
from django.db.models import Sum, F


def get_revenue_by_subscription_type_current_year():

    current_year = datetime.now().year

    # Filtra los pagos que pertenecen a suscripciones que comenzaron en el año actual
    payments = Payment.objects.filter(subscription__start_date__year=current_year)

    # Agrupa los pagos por tipo de suscripción y suma los montos de los pagos
    subscription_revenue = payments.values('subscription__subscription_type__name').annotate(revenue=Sum('price')).order_by('subscription__subscription_type__name')

    # Prepara los datos en el formato deseado
    revenue_data = [{'subscription_type': item['subscription__subscription_type__name'], 'revenue': float(item['revenue'])} for item in subscription_revenue]

    # Convierte los datos a formato JSON
    revenue_data_json = json.dumps(revenue_data)

    return revenue_data_json
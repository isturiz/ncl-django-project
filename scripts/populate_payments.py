import random
from datetime import date, timedelta, datetime
from django.db import transaction
from home.models import Subscription, Payment

# Obtén todas las suscripciones existentes
subscriptions = Subscription.objects.all()

# Define la duración de una suscripción en días (1 mes)
subscription_duration = 250

# Define la fecha actual
current_date = datetime.now()

# Genera pagos aleatorios para las suscripciones existentes
with transaction.atomic():
    for subscription in subscriptions:
        # Calcula la fecha de inicio y finalización de la suscripción
        start_date = subscription.start_date
        end_date = subscription.end_date

        # Crea pagos aleatorios para la suscripción
        num_payments = random.randint(1, 2)  # Entre 1 y 6 pagos
        for _ in range(num_payments):
            payment_date = start_date - timedelta(days=random.randint(0, subscription_duration - 1))
            payment_amount = subscription.subscription_type.price
            payment = Payment(
                price=payment_amount,
                date=payment_date,
                subscription=subscription
            )
            payment.save()


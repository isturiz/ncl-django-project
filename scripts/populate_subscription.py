import random
from datetime import date, timedelta
from django.db import transaction
from faker import Faker
from apps.home.models import Student, SubscriptionType, Subscription

fake = Faker()

# Obtén estudiantes activos
active_students = Student.objects.filter(is_active=True)

# Obtén tipos de suscripción disponibles
subscription_types = SubscriptionType.objects.all()

# Define la duración de una suscripción en días (1 mes)
subscription_duration = 30

# Define la fecha actual
current_date = date.today()

# Genera suscripciones aleatorias
with transaction.atomic():
    for student in active_students:
        # Elige aleatoriamente 1 o 2 tipos de suscripción
        num_subscriptions = random.randint(1, 2)
        selected_types = random.sample(list(subscription_types), num_subscriptions)
        
        for subscription_type in selected_types:
            # Calcula la fecha de inicio y finalización
            start_date = current_date - timedelta(days=random.randint(0, subscription_duration - 1))
            end_date = start_date + timedelta(days=subscription_duration)
            
            # Crea la suscripción
            subscription = Subscription(
                subscription_type=subscription_type,
                student=student,
                start_date=start_date,
                end_date=end_date,
                # subscription_status=end_date >= current_date,


            )
            subscription.save()
        
# 


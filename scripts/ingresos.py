from django.db.models import Sum
from home.models import Subscription, Lesson, Payment



# Calcular los ingresos de las suscripciones
total_subscription_income = Subscription.objects.aggregate(
    total=Sum('payments__price')
)['total']

# Calcular los ingresos de las lecciones
total_lesson_income = Lesson.objects.aggregate(
    total=Sum('price')
)['total']


total_payment = Payment.objects.aggregate(
    total=Sum('price')
)['total']

# Calcular los ingresos totales
total_income = total_subscription_income + total_lesson_income

print(f'Ingresos estimados totales: ${total_income}')
print(f'Ingresos reales totales: ${total_payment}')


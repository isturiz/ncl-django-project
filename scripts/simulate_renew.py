from apps.home.models import Subscription
from datetime import date

latest_subscription = Subscription.objects.order_by('-id').first()

if latest_subscription:
    # Configura las fechas para simular un escenario de renovación
    # latest_subscription.start_date = date(2023, 11, 1)
    # latest_subscription.end_date = date(2023, 11, 31)

    # Llama a la función de renovación
    latest_subscription.renew_subscription()
    print("La suscripción ha sido renovada.")
    print(latest_subscription)
else:
    print("No se encontraron registros de Subscription en la base de datos.")

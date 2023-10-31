from apps.home.models import SubscriptionType

def populate_subscription_types():
    SubscriptionType.objects.create(name="Suscripción para clases únicas", description="Suscripción para clases únicas", price="0")

    SubscriptionType.objects.create(name="Particular en Casa", description="Suscripción para clases particulares en la casa del estudiante", price="50", number_of_lessons="4")
    SubscriptionType.objects.create(name="Particular en Academia", description="Suscripción para clases particulares en la academia", price="40", number_of_lessons="4")
    SubscriptionType.objects.create(name="Particular Virtual", price="50", description="Suscripción para clases virtuales", number_of_lessons="4")

    SubscriptionType.objects.create(name="Grupal en Academia", description="Suscripción para clases grupales en la academia", price="30", number_of_lessons="8")


    print("SubscriptionType data added successfully.")

populate_subscription_types()
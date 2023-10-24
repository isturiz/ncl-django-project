from home.models import SubscriptionType

def populate_subscription_types():
    SubscriptionType.objects.create(name="Suscripción para clases únicas", description="Suscripción para clases únicas", price="0")
    SubscriptionType.objects.create(name="Particular en Casa", description="Suscripción para clases particulares en la casa del estudiante", price="40", number_of_lessons="6")
    SubscriptionType.objects.create(name="Presencial en Academia", description="Suscripción para clases presenciales en la academia", price="20", number_of_lessons="4")
    SubscriptionType.objects.create(name="Virtual", price="30", description="Suscripción para clases particulares virtuales", number_of_lessons="2")

    print("SubscriptionType data added successfully.")

populate_subscription_types()
from home.models import SubscriptionType

def populate_subscription_types():
    SubscriptionType.objects.create(name="Particular en Casa", price="40", number_of_lessons="6")
    SubscriptionType.objects.create(name="Presencial en Academia", price="20", number_of_lessons="4")
    SubscriptionType.objects.create(name="Virtual por meet", price="30", number_of_lessons="2")

    print("SubscriptionType data added successfully.")

populate_subscription_types()
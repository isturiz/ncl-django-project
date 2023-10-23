from django.test import TestCase
from datetime import date, timedelta
from home.models import Subscription, SubscriptionType, Student

class SubscriptionModelTest(TestCase):

    def setUp(self):
        # Crea objetos SubscriptionType, Student, y Subscription para probar
        subscription_type = SubscriptionType.objects.create(name='Tipo de suscripción', price=10)
        student = Student.objects.create(name='Nombre del estudiante')
        start_date = date(2023, 1, 1)
        end_date = date(2023, 1, 31)
        self.subscription = Subscription.objects.create(subscription_type=subscription_type, student=student, start_date=start_date, end_date=end_date)

    def test_renew_subscription(self):
        # Configura el auto_renewal en True
        self.subscription.auto_renewal = True
        self.subscription.save()

        # Llama a la función renew_subscription
        self.subscription.renew_subscription()

        # Verifica que se haya creado una nueva Subscription
        new_subscription = Subscription.objects.latest('id')
        self.assertTrue(new_subscription)

        # Verifica que los campos de la nueva Subscription son correctos 
        self.assertEqual(new_subscription.subscription_type, self.subscription.subscription_type)
        self.assertEqual(new_subscription.student, self.subscription.student)
        self.assertEqual(new_subscription.is_active, True)
        self.assertEqual(new_subscription.auto_renewal, True)

        # Verifica que las fechas de inicio y finalización sean correctas
        expected_start_date = self.subscription.end_date + timedelta(days=1)
        expected_end_date = self.subscription.end_date + timedelta(days=31)
        self.assertEqual(new_subscription.start_date, expected_start_date)
        self.assertEqual(new_subscription.end_date, expected_end_date)

from home.models import Lesson, LessonType, Subscription, Teacher

lesson_type = LessonType.objects.get(pk=1)
subscription_type = Subscription.objects.get(pk=4)
teacher = Teacher.objects.get(pk=1)

# Crear una instancia de Lesson
lesson = Lesson.objects.create(lesson_type=lesson_type, price=100)

# Obtener o crear una instancia de Subscription
subscription, created = Subscription.objects.get_or_create(type_subscription=subscription_type)

# Crear una instancia de LessonXSubscription para relacionar la lección y la suscripción
lesson_subscription = LessonXSubscription.objects.create(lesson=lesson, subscription=subscription, teacher=teacher)

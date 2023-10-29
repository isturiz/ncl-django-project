# scripts/populate_lessons.py
import random
from home.models import Lesson, LessonType

def populate_lessons():
    lesson_types = LessonType.objects.all()

    for _ in range(5):
        random_lesson_type = LessonType.objects.order_by('?').first()  # Selecciona aleatoriamente un LessonType
        Lesson.objects.create(
            lesson_type=random_lesson_type,
            description="Descripción de la lección",  # Reemplaza con la descripción deseada
            price=30.00,  # Precio de la lección (ajusta según tus necesidades)
            start_date=None,  # Fecha de inicio (puedes ajustarla)
            end_date=None,  # Fecha de finalización (puedes ajustarla)
            lesson_status=True,  # Cambia esto según tus necesidades (True o False)
        )

    print("Lesson data added successfully.")

populate_lessons()

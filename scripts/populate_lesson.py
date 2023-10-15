# scripts/populate_lessons.py
import random
from home.models import Lesson, LessonType

def populate_lessons():
    lesson_types = LessonType.objects.all()

    for _ in range(5):
        random_lesson_type = random.choice(lesson_types)
        Lesson.objects.create(
            lesson_type=random_lesson_type,
            price=random.uniform(30.00, 100.00)
        )

    print("Lesson data added successfully.")

populate_lessons()

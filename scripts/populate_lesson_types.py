from home.models import LessonType

def populate_lesson_types():
    LessonType.objects.create(cathedra="Piano", modality="Virtual")
    LessonType.objects.create(cathedra="Piano", modality="Particular en Casa")
    LessonType.objects.create(cathedra="Piano", modality="Presencial en Academia")
    LessonType.objects.create(cathedra="Cuatro", modality="Virtual")
    LessonType.objects.create(cathedra="Cuatro", modality="Particular en Casa")
    LessonType.objects.create(cathedra="Cuatro", modality="Presencial en Academia")

    print("LessonType data added successfully.")

populate_lesson_types()
from home.models import Teacher

def populate_teachers():
    Teacher.objects.create(
        identify_card="1111",
        first_name="Juan",
        second_name="Carlos",
        first_surname="Gómez",
        second_surname="López",
        birthdate="1985-04-10",
        phone_number="555-1111",
        email="juan@example.com",
        address="123 Main St",
        is_active=True
    )

    Teacher.objects.create(
        identify_card="2222",
        first_name="María",
        second_name="Isabel",
        first_surname="Sánchez",
        second_surname="Martínez",
        birthdate="1990-07-22",
        phone_number="555-2222",
        email="maria@example.com",
        address="456 Elm St",
        is_active=True
    )

    Teacher.objects.create(
        identify_card="3333",
        first_name="Luis",
        second_name="Antonio",
        first_surname="Ramírez",
        second_surname="García",
        birthdate="1978-02-15",
        phone_number="555-3333",
        email="luis@example.com",
        address="789 Oak St",
        is_active=True
    )

    Teacher.objects.create(
        identify_card="4444",
        first_name="Laura",
        second_name="Margarita",
        first_surname="Gómez",
        second_surname="Fernández",
        birthdate="1986-11-28",
        phone_number="555-4444",
        email="laura@example.com",
        address="890 Cedar St",
        is_active=True
    )

    Teacher.objects.create(
        identify_card="5555",
        first_name="Carlos",
        second_name="Fernando",
        first_surname="Pérez",
        second_surname="Hernández",
        birthdate="1975-05-20",
        phone_number="555-5555",
        email="carlos@example.com",
        address="111 Pine St",
        is_active=True
    )

    print("Teacher data added successfully.")


populate_teachers()

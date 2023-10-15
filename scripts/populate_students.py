# scripts/populate_students.py

from home.models import Student

def populate_students():
    Student.objects.create(
        identify_card="",
        first_name="Juan",
        second_name="Pedro",
        first_surname="Gómez",
        second_surname="López",
        birthdate="1990-01-15",
        phone_number="555-1234",
        email="juan@example.com",
        address="123 Main St",
        is_active=True
    )

    Student.objects.create(
        identify_card="7654321",
        first_name="María",
        second_name="Elena",
        first_surname="Sánchez",
        second_surname="Martínez",
        birthdate="1995-02-28",
        phone_number="555-5678",
        email="maria@example.com",
        address="456 Elm St",
        is_active=True
    )

    Student.objects.create(
        identify_card="1112223",
        first_name="Carlos",
        second_name="Antonio",
        first_surname="López",
        second_surname="Rodríguez",
        birthdate="1997-05-20",
        phone_number="555-1111",
        email="carlos@example.com",
        address="111 Pine St",
        is_active=True
    )

    Student.objects.create(
        identify_card="2223334",
        first_name="Laura",
        second_name="Margarita",
        first_surname="Gómez",
        second_surname="Fernández",
        birthdate="2000-07-15",
        phone_number="555-2222",
        email="laura@example.com",
        address="222 Maple St",
        is_active=True
    )

    print("Student data added successfully.")


populate_students()
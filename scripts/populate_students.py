# scripts/populate_students.py

from home.models import Student
from datetime import date, datetime, timedelta
import random
from faker import Faker

faker = Faker()



FIRST_NAMES = [
    'Carlos',
    'Luis',
    'Ana',
    'Pedro',
    'Camila',
    'Juan',
    'María',
    'Lorena',
    'José',
    'Javier',
    'Miguel',
    'Luisa',
    'Luciano',
    'Marcos',
    'Sofía',
    'Daniel',
    'Marina',
    'Elena',
    'Isabel',
    'Fernando',
    'Laura',
    'Xeniel'
    'Sara',
    'Alejandra',
    'Ricardo',
    'Mariana',
    'Raul',
    'Gabriel',
    'Axel',
    'Natalia',
    'Eduardo',
    ]

LAST_NAME = [
    'Gonzales',
    'Martínez',
    'Torres',
    'Fernández',
    'Hernández',
    'López',
    'García',
    'Pérez',
    'Gómez',
    'Rojas',
    'Muñoz',
    'Sánchez',
    'Rivera',
    'Vega',
    'Martín',
    'Ramírez',
    'Mendoza',
    'Navarro',
    'Morales',
    'Riera',
    'Flores',
    'Mora',
    'Cruz',
    'Aquino',
    'Istúriz',
    'Dorante',
    'Figueroa',
    'Velázquez',
    'Villegas',
    ]

ADDRESS = [
    'Urbanización Ciudad Roca, Barquisimeto',
    'Calle de los Niños, Urbanización Los Próceres, Barquisimeto',
    'Avenida Venezuela, Centro Comercial El Trigal, Barquisimeto',
    'Calle Los Estudiantes, Urbanización Los Próceres, Barquisimeto',
    'Urbanización El Trigal, Barquisimeto',
    'Calle de la Luna, Urbanización Los Próceres, Barquisimeto',
    'Urbanización Yucatán, Barquisimeto',
    'Urbanización Roquita, Barquisimeto',
    'Urbanización Nueva Tierra, Barquisimeto',
    'Urbanización Tierra Vieja, Barquisimeto',
    'Urbanización La Grieta del Invocador',
]

def generate_phone_number():
    prefixe = ['0412', '0416', '0424', '0414', '0416']
    prefixe = random.choice(prefixe)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])

    telefono = f'{prefixe}-{number}'
    return telefono

def generate_identify_card():
    random_number = random.randint(33000000, 39000000)
    random_string = f"V-{random_number:07}"

    return random_string

def generate_first_name():
    return random.choice(FIRST_NAMES)

def generate_last_name():
    return random.choice(LAST_NAME)

def generate_birthdate():
    return date(random.randint(2007, 2019), random.randint(1, 12), random.randint(1, 28))

def generate_address():
    return random.choice(ADDRESS)

def generate_email():
    return faker.email()

def generate_boolean():
    threshold = 0.8  # 80% probability of True
    random_number = random.random()  # Generate a random number between 0 and 1
    return True if random_number < threshold else False

def populate_students():
    for i in range(20):
        Student.objects.create(
            identify_card=generate_identify_card(),
            first_name=generate_first_name(),
            second_name=generate_first_name(),
            first_surname=generate_last_name(),
            second_surname=generate_last_name(),
            birthdate=generate_birthdate(),
            phone_number=generate_phone_number(),
            email=generate_email(),
            address=generate_address(),
            is_active=generate_boolean()
        )

    print("Student data added successfully.")

populate_students()
from apps.home.models import Student


from datetime import date
import random
from faker import Faker
from faker.providers import DynamicProvider

fake = Faker('es_ES')

custom_first_names_provider= DynamicProvider(
    provider_name="custom_first_names",
    elements=[
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
)
fake.add_provider(custom_first_names_provider)

custom_last_names_provider = DynamicProvider(
    provider_name="custom_last_names",
    elements=[
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
)
fake.add_provider(custom_last_names_provider)


custom_address_provider = DynamicProvider(
    provider_name = "custom_address",
    elements = [
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
)
fake.add_provider(custom_address_provider)

def generate_phone_number():
    prefixe = ['0412', '0416', '0424', '0414', '0416']
    prefixe = random.choice(prefixe)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])

    telefono = f'{prefixe}{number}'
    return telefono

def generate_identify_card(initial, final):
    random_number = random.randint(initial, final)
    random_string = f"V{random_number:07}"

    return random_string

def generate_first_name():
    return fake.custom_first_names()

def generate_last_name():
    return fake.custom_last_names()

def generate_birthdate(years):
    return date(random.randint(years[0], years[1]), random.randint(1, 12), random.randint(1, 28))

def generate_address():
    return fake.custom_address()

def generate_email():
    return fake.email()

def generate_boolean():
    threshold = 0.8  # 80% probability of True
    random_number = random.random()  # Generate a random number between 0 and 1
    return True if random_number < threshold else False

def populate_students():
    for i in range(20):
        Student.objects.create(
            identify_card=generate_identify_card(33000000, 39000000),
            first_name=generate_first_name(),
            second_name=generate_first_name(),
            first_surname=generate_last_name(),
            second_surname=generate_last_name(),
            birthdate=generate_birthdate(years=[2007, 2019]),
            phone_number=generate_phone_number(),
            email=generate_email(),
            address=generate_address(),
            is_active=generate_boolean()
        )

    print("Student data added successfully.")

populate_students()
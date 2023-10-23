from home.models import Student, Subscription
from home.models import Student

from datetime import datetime
from django.db.models import Count
from django.db.models.functions import ExtractYear
import json


def get_start_dates_for_students():
    students = Student.objects.all()
    start_dates = []
    for student in students:
        subscriptions = Subscription.objects.filter(student=student).order_by('start_date')
        if subscriptions.exists():
            first_subscription = subscriptions.first()
            start_dates.append({
                'student_name': str(student),
                'start_date': first_subscription.start_date,
            })
    return start_dates

def calculate_age_by_count():
    today = datetime.now()

    # Calculate the age of the students and group by age
    students = Student.objects.annotate(age=ExtractYear(today) - ExtractYear('birthdate')).values('age').annotate(count=Count('id')).order_by('age')

    # Prepape the data in the desired format
    age_data = [{'age': student['age'], 'count': student['count']} for student in students]
    age_data_json = json.dumps(age_data)
    
    return age_data_json

def get_student_count_by_subscription_type():
    subscription_counts = Student.objects.values('subscription__subscription_type__name').annotate(count=Count('id')).order_by('subscription__subscription_type__name')

    # Prepara los datos en el formato deseado
    subscription_data = [{'subscription_type': item['subscription__subscription_type__name'], 'count': item['count']} for item in subscription_counts]

    # Convierte los datos a formato JSON
    subscription_data_json = json.dumps(subscription_data)

    # Devuelve los datos en formato JSON
    return subscription_data_json

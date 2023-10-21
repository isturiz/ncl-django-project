from home.models import Student, Subscription
from home.models import Student

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
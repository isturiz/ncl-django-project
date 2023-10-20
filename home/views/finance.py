from django.views.generic import TemplateView

from datetime import datetime, timedelta


from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from json import dumps

from home.models import Subscription, Payment, Student

# Months to days
THREE_MONTHS = 90
SIX_MONTHS = 180
NINE_MONTHS = 270

class FinanceView(TemplateView):
    template_name = 'home/finance.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ### Payments info
        context['payment_data'] = self.get_all_payment_data()
        context['percentage_change'] = self.calculate_percentage_change()

        # Total amount per month
        context['total_payments_current_year'] = self.get_total_payments_current_year() 
        context['total_payments_amount_last_three_months'] = self.get_total_payments_amount_last_three_months() 
        context['total_payments_amount_last_six_months'] = self.get_total_payments_amount_last_six_months() 
        context['total_payments_amount_last_nine_months'] = self.get_total_payments_amount_last_nine_months() 

        # Data per month
        context['monthly_payment_data'] = self.get_monthly_payment_data_current_year()
        context['payments_data_last_three_months'] = self.get_total_payments_last_three_months()
        context['payments_data_last_six_months'] = self.get_total_payments_last_six_months()
        context['payments_data_last_nine_months'] = self.get_total_payments_last_nine_months()

        ### Students info
        context['inscription_students'] = self.get_start_dates_for_students()

        return context

    def get_start_dates_for_students(self):
        # Obtener todos los estudiantes
        students = Student.objects.all()
        
        # Crear una lista para almacenar las fechas de inicio de los estudiantes
        start_dates = []

        # Recorrer todos los estudiantes y obtener sus fechas de inicio
        for student in students:
            subscriptions = Subscription.objects.filter(student=student).order_by('start_date')
            if subscriptions.exists():
                first_subscription = subscriptions.first()
                start_dates.append({
                    'student_name': str(student),
                    'start_date': first_subscription.start_date,
                })
        
        return start_dates
    
    def get_total_payments_historically(self):
        total_payments = Payment.objects.aggregate(total=models.Sum('price'))
        return total_payments['total'] or 0

    # Total payments amount for current year
    def get_total_payments_current_year(self):
        current_year = datetime.now().year
        total_payments = Payment.objects.filter(date__year=current_year).aggregate(total=Sum('price'))
        return total_payments['total'] or 0
    
    # Total payments amount for last months (main function)
    def get_total_payments_amount_last_months(self, months):
        today = datetime.now()
        months_ago = today - timedelta(days=months)
        total_payments = Payment.objects.filter(date__range=[months_ago, today]).aggregate(total=Sum('price'))
        return total_payments['total'] or 0

    # Total payments amount for last three months
    def get_total_payments_amount_last_three_months(self):
        return self.get_total_payments_amount_last_months(THREE_MONTHS)
    
    # Total payments amount for last six months
    def get_total_payments_amount_last_six_months(self):
        return self.get_total_payments_amount_last_months(SIX_MONTHS)
    
    # Total payments amount for last nine months
    def get_total_payments_amount_last_nine_months(self):
        return self.get_total_payments_amount_last_months(NINE_MONTHS)



    def get_all_payment_data(self):
        payments = Payment.objects.all()
        payment_data = [
            {
                'price': float(payment.price),
                'subscription': str(payment.subscription),
                'date': payment.date.strftime("%Y-%m-%d %H:%M:%S")
            } for payment in payments
        ]
        return dumps(payment_data)

    # Payment data for each month of current year
    def get_monthly_payment_data_current_year(self):
        current_year = datetime.now().year
        monthly_payments = Payment.objects.filter(date__year=current_year) \
            .annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))
        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        return dumps(monthly_payment_data)
    
    # Payment data for last months of current year (main function)
    def get_total_payments_last_months(self, months):
        today = datetime.now()
        months_ago = today - timedelta(days=months)

        monthly_payments = Payment.objects.filter(date__range=[months_ago, today]) \
            .annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))

        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        
        return dumps(monthly_payment_data)
    
    # Payment data for last three months of current year
    def get_total_payments_last_three_months(self):
        return self.get_total_payments_last_months(90)
    
    # Payment data for last six months of current year
    def get_total_payments_last_six_months(self):
        return self.get_total_payments_last_months(180)
    
    # Payment data for last nine months of current year
    def get_total_payments_last_nine_months(self):
        return self.get_total_payments_last_months(270)
    
    
    # All payment data for each month historically
    def get_monthly_payment_data_historical_month(self):
        monthly_payments = Payment.objects.annotate(month=ExtractMonth('date')) \
            .annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))
        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        return dumps(monthly_payment_data)
    
    # Calculate percentage change per last month 
    def calculate_percentage_change(self):
        today = datetime.now()
        this_month_payments = Payment.objects.filter(date__month=today.month, date__year=today.year).aggregate(total=Sum('price'))['total'] or 0
        last_month = today - timedelta(days=today.day)
        last_month_payments = Payment.objects.filter(date__month=last_month.month, date__year=last_month.year).aggregate(total=Sum('price'))['total'] or 0
        if last_month_payments > 0:
            return round(((this_month_payments - last_month_payments) / last_month_payments) * 100, 2)
        else:
            return 0
from celery import Task
from datetime import datetime
from home.models import Subscription

task = Task()

@task
def auto_renew_subscriptions():
    current_date = datetime.now().date()

    subscriptions_to_renew = Subscription.objects.filter(auto_renewal=True, end_date=current_date)

    for subscription in subscriptions_to_renew:
        subscription.renew_subscription()

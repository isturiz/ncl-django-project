# Generated by Django 4.2.5 on 2023-10-27 18:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0018_subscription_unique_subscription"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="subscription",
            name="unique_subscription",
        ),
    ]
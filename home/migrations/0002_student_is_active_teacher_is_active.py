# Generated by Django 4.2.5 on 2023-10-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="teacher",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]

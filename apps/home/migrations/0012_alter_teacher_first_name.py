# Generated by Django 4.2.5 on 2023-10-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_alter_student_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="first_name",
            field=models.CharField(max_length=255, verbose_name="First Name"),
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_alter_student_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-22 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="LessonType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="LessonXDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cost", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.lesson"
                    ),
                ),
                (
                    "lesson_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.lessontype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("second_name", models.CharField(blank=True, max_length=50)),
                ("first_surname", models.CharField(max_length=50)),
                ("second_surname", models.CharField(blank=True, max_length=50)),
                ("birthdate", models.DateField()),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=8)),
                ("subscription_status", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identify_card", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=50)),
                ("second_name", models.CharField(blank=True, max_length=50)),
                ("first_surname", models.CharField(max_length=50)),
                ("second_surname", models.CharField(blank=True, max_length=50)),
                ("birthdate", models.DateField()),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="TeacherXDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lesson_x_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.lessonxdetail",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.teacher"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubscriptionXDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lesson_x_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.lessonxdetail",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.subscription",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentXDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("description", models.CharField(max_length=200)),
                ("student_status", models.CharField(max_length=50)),
                (
                    "lesson_x_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.lessonxdetail",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.student"
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.subscription",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RenewSubscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subscription_amount",
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                ("end_date", models.DateField()),
                ("number_of_months", models.PositiveIntegerField()),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.subscription",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=8)),
                ("date", models.DateField()),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.subscription",
                    ),
                ),
            ],
        ),
    ]

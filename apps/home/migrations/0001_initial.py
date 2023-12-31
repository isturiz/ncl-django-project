# Generated by Django 4.2.5 on 2023-11-01 17:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActivityLog",
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
                ("action", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
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
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Price",
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Start Date"
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="End Date"
                    ),
                ),
                (
                    "lesson_status",
                    models.BooleanField(default=False, verbose_name="Lesson Status"),
                ),
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
                ("cathedra", models.CharField(max_length=255, verbose_name="Cathedra")),
                ("modality", models.CharField(max_length=255, verbose_name="Modality")),
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
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="Date")),
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
                (
                    "identify_card",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Identify Card",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "second_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Second Name",
                    ),
                ),
                (
                    "first_surname",
                    models.CharField(max_length=255, verbose_name="First Surname"),
                ),
                (
                    "second_surname",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Second Surname",
                    ),
                ),
                ("birthdate", models.DateField(verbose_name="Birthdate")),
                ("phone_number", models.CharField(max_length=20, verbose_name="Phone")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("address", models.TextField(verbose_name="Address")),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
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
                ("start_date", models.DateField(verbose_name="Start Date")),
                ("end_date", models.DateField(verbose_name="End Date")),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "auto_renewal",
                    models.BooleanField(default=True, verbose_name="Auto Renewal"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubscriptionType",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Price",
                    ),
                ),
                (
                    "number_of_lessons",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Number of Lessons"
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
                (
                    "identify_card",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        unique=True,
                        verbose_name="Identify Card",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "second_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Second Name",
                    ),
                ),
                (
                    "first_surname",
                    models.CharField(max_length=255, verbose_name="First Surname"),
                ),
                (
                    "second_surname",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Second Surname",
                    ),
                ),
                ("birthdate", models.DateField(verbose_name="Birthdate")),
                ("phone_number", models.CharField(max_length=20, verbose_name="Phone")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("address", models.TextField(verbose_name="Address")),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=254, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="last name"),
                ),
                (
                    "last_login",
                    models.DateField(
                        auto_now=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ST", "Student"),
                            ("TC", "Teacher"),
                            ("DR", "Director"),
                            ("AD", "Administrator"),
                        ],
                        default="ST",
                        max_length=2,
                        verbose_name="role",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="staff status"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="customuser_groups",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="customuser_user_permissions",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.AddConstraint(
            model_name="teacher",
            constraint=models.UniqueConstraint(
                fields=(
                    "identify_card",
                    "first_name",
                    "second_name",
                    "first_surname",
                    "second_surname",
                    "birthdate",
                ),
                name="unique_teacher",
            ),
        ),
        migrations.AddConstraint(
            model_name="subscriptiontype",
            constraint=models.UniqueConstraint(
                fields=("name", "price"), name="unique_subscription_type"
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="home.student",
                verbose_name="Student",
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="subscription_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="home.subscriptiontype",
                verbose_name="Subscription Type",
            ),
        ),
        migrations.AddConstraint(
            model_name="student",
            constraint=models.UniqueConstraint(
                fields=(
                    "identify_card",
                    "first_name",
                    "second_name",
                    "first_surname",
                    "second_surname",
                    "birthdate",
                ),
                name="unique_student",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="subscription",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to="home.subscription",
                verbose_name="Subscription",
            ),
        ),
        migrations.AddConstraint(
            model_name="lessontype",
            constraint=models.UniqueConstraint(
                fields=("cathedra", "modality"), name="unique_lesson_type"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="lesson_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="home.lessontype",
                verbose_name="Lesson Type",
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="subscription",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="home.subscription",
                verbose_name="Subscription",
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="home.teacher",
                verbose_name="Teacher",
            ),
        ),
        migrations.AddField(
            model_name="activitylog",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.user"
            ),
        ),
    ]

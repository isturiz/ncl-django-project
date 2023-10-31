from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts", include("apps.accounts.urls")),

    path("home/", include("apps.home.urls")),

    path("students/", include("apps.students.urls")),
    path("teachers/", include("apps.teachers.urls")),

    path("lessons/", include("apps.lessons.urls")),
    path("lesson_types/", include("apps.lesson_types.urls")),
    path("fullcalendar/", include("apps.fullcalendar.urls")),

    path("payments/", include("apps.payments.urls")),

    path("subscriptions/", include("apps.subscriptions.urls")),
    path("subscription_types/", include("apps.subscription_types.urls")),

    path("users/", include("apps.users.urls")),
    path("activity_logs/", include("apps.activity_logs.urls")),

    path("reports/", include("apps.reports.urls")),

]

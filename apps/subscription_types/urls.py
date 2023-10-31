from django.urls import path

from .views import SubscriptionTypes_ListView, SubscriptionTypes_CreateView, SubscriptionTypes_UpdateView

urlpatterns = [
    path('', SubscriptionTypes_ListView.as_view(), name='subscription-types-list'),
    path('create/', SubscriptionTypes_CreateView.as_view(), name='subscription-types-create'),
    path('update/<int:pk>/', SubscriptionTypes_UpdateView.as_view(), name='subscription-types-update'),
]
from django.urls import path

from .views import Subscription_ListView, Subscription_CreateView, Subscription_UpdateView

urlpatterns = [
    path('', Subscription_ListView.as_view(), name='subscription-list'),
    path('create/', Subscription_CreateView.as_view(), name='subscription-create'),
    path('update/<int:pk>/', Subscription_UpdateView.as_view(), name='subscription-update'),
]
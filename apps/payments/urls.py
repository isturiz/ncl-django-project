

# accounts/urls.py
from django.urls import path
from .views import Payment_ListView, Payment_CreateView, Payment_UpdateView, FinanceView



urlpatterns = [

    path('finances/', FinanceView.as_view(), name='finances'),

    path('', Payment_ListView.as_view(), name='payment-list'),
    path('create/', Payment_CreateView.as_view(), name='payment-create'),
    path('update/<int:pk>/', Payment_UpdateView.as_view(), name='payment-update'),
]
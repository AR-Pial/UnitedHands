from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
	path('make-donation',views.payment,name='payment'),
	path('payment/paypal-payment/', views.paypal_payment, name='paypal_payment'),
]

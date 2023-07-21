from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    payments = Payment.objects.all().order_by('-timestamp')
    context = {
        "payments":payments
    }
    return render(request,'home.html',context)

def payment(request):
    return render(request,'payment.html')

@csrf_exempt
def paypal_payment(request):
    if request.method == 'POST':
        # Retrieve transaction details from the PayPal JavaScript SDK
        transaction_id = request.POST.get('orderID')
        payer_name = request.POST.get('payer_name')
        payer_email = request.POST.get('payer_email')
        payer_phone = request.POST.get('payer_phone')
        amount = float(request.POST.get('amount'))

        # Save the payment details to the database
        payment = Payment.objects.create(
            amount=amount,
            payer_name=payer_name,
            payer_email=payer_email,
            payer_phone=payer_phone,
            transaction_id=transaction_id,
            payment_status=True  # You may need to modify this based on PayPal's status response
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

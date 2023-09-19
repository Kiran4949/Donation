from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


# Create your views here.

# Paypal email id[to donate] :- testingofshopkproject2@gmail.com   &   password :- Shopk@4994



def home(request):
    return render(request, 'home.html')


def donate(request):
    if request.method == 'POST':
        try:
            transaction_completed = True

            if transaction_completed:
                user_email = request.user.email

                subject = 'Donation Confirmation'
                message = 'Thank you for your donation!'
                from_email = settings.EMAIL_HOST_USER  
                recipient_list = [user_email]

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                messages.success(request, 'Donation successful. Check your email for confirmation.')
            else:
                messages.error(request, 'Transaction failed.')

            return redirect('donate')  
        except Exception as e:
            messages.error(request, 'An error occurred during the transaction: ' + str(e))

    return render(request, 'donate.html')






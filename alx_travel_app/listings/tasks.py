from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_confirmation(email):
    send_mail(
        'Payment Successful',
        'Your booking payment was successful.',
        'noreply@travelapp.com',
        [email],
        fail_silently=True,
    )

@shared_task
def send_booking_confirmation_email(customer_email, booking_details):
    """
    Sends an asynchronous email confirmation for a new booking.
    """
    subject = 'Booking Confirmation - ALX Travel App'
    message = f"Thank you for your booking!\n\nDetails: {booking_details}"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]
    
    send_mail(subject, message, email_from, recipient_list)
    return f"Email sent to {customer_email}"

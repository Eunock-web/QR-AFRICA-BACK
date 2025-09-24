import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings

def generateOtp():
    otp = ""
    for i in range(1,6):
        otp += str(random.randint(1, 9)) 
    return otp


def send_otp_email(email):
    subject = "One time passcode for Email verification"
    otp = generateOtp()
    user = User.objects.get(email=email)
    current_site = "myauth.com"
    message = f"Your one time passcode is {otp}"
    from_email = settings.DEFAULT_FROM_EMAIL
    
    OneTimePassword.objects.create(user=user, otp=otp)
    send_email = EmailMessage(subject = subject, message = message, from_email = from_email, to=[email])
    send_email.send()
    return otp
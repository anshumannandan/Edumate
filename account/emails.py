from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from django.conf import settings
from . models import User

class EMAIL:
    @staticmethod
    def send_otp_via_email(mailaddress):
        otp = random.randint(1000,9999)
        user = User.objects.get(email = mailaddress)
        user=user.name

        html_content = render_to_string("email_template.html",{"otp": otp, "user": user})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "EDUMATE PASSWORD RESET",
            text_content,
            settings.EMAIL_HOST,
            [mailaddress]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        user = User.objects.get(email=mailaddress)
        user.otp = otp
        user.save()
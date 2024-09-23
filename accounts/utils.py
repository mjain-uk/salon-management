from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

account_activation_token = TokenGenerator()

class AccountActivationUtils:

    @staticmethod
    def send_activation_email(user, request):
        """Send activation email with clickable link to the user."""
        registration_token = account_activation_token.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = f"http://{request.get_host()}{reverse('activate', kwargs={'uidb64': uid, 'token': registration_token})}"

        # Email content with clickable link
        subject = 'Activate your MBK account'
        message = f"""
        <p>Thank you for registering with us.</p>
        <p>Click the link below to activate your account:</p>
        <p><a href="{activation_url}" target="_blank">Activate your account</a></p>
        """
        
        # Send the email
        send_mail(
            subject,
            '',  # Empty plaintext message (use HTML only)
            'info@makeupbykopal.com',
            [user.email],
            fail_silently=False,
            html_message=message  # Send HTML email
        )



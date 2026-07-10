from twilio.rest import Client
from django.conf import settings


def send_sms(to, message):
    # ❌ Disable SMS completely if not enabled
    if not getattr(settings, "ENABLE_SMS", False):
        return

    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to
    )

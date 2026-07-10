from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ExternalBooking
from .utils import send_sms


@receiver(post_save, sender=ExternalBooking)
def payment_status_sms(sender, instance, created, **kwargs):
    if created:
        return

    if instance.payment_status == "verified":
        send_sms(
            f"+91{instance.mobile}",
            f"Your turf booking on {instance.date} "
            f"({instance.slot}) is CONFIRMED. Thank you!"
        )

    elif instance.payment_status == "rejected":
        send_sms(
            f"+91{instance.mobile}",
            f"Your turf booking on {instance.date} "
            f"({instance.slot}) was REJECTED. Please contact admin."
        )

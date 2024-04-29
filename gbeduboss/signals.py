from django.dispatch import receiver

from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

from beatcart.models import *

@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    ipn = sender

    if ipn.payment_status == 'completed':
        Beatcart.objects.create()
        Albumcart.objects.create()


@receiver(invalid_ipn_received)
def invalid_ipn_signal(sender, **kwargs):
    ipn = sender

    if ipn.payment_status == 'completed':
        Beatcart.objects.create()
        Albumcart.objects.create()
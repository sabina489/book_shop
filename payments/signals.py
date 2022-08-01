from django.db.models.signals import post_save
from django.dispatch import receiver
from cart.models import Cart
from payments.models import Payment

@receiver(post_save, sender="payments.payment")
def payment(sender,instance,**kwargs):
    if instance.status == "paid":
        instance.order.order_status = "success"
        print("Successful")
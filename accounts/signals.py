from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Member
from .models import generate_readable_id

@receiver(pre_save, sender=Member)
def generate_unique_id(sender, instance, **kwargs):
    if not instance.unique_id:
        instance.unique_id = generate_readable_id()
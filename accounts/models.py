from django.db import models

# Create your models here.

import uuid
import random
import string
from django.db import models
from django.utils import timezone


def generate_readable_id(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unique_id = models.CharField(max_length=32, unique=True, blank=True)
    email = models.EmailField(unique=True)


    is_active = models.BooleanField(default=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    referral_code = models.CharField(max_length=20, blank=True, null=True)
    invite_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email
    


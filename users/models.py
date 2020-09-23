from django.contrib.auth.models import User
from django.db.models.signals import pre_save


def save_profile(sender, instance, **kwargs):
    email = instance.email.split('@')[0]

    instance.username = email


pre_save.connect(save_profile, sender=User)
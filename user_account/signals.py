from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserAccount

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(pk=instance.pk)
        instance.useraccount.save()
    # Esto se ejecuta cada vez que un User es guardado. 
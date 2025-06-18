from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Additional fields for user account
    birth_date = models.DateField(null=True, blank=True)  # Optional field for date of birth
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            # Intenta devolver el username del usuario relacionado.
            return self.user.username
        except User.DoesNotExist:
            # Esto ocurre si el objeto User relacionado fue eliminado (y la cascada no funcionó o fue manual)
            return f"UserAccount (ID: {self.pk} - Usuario Eliminado)"
        except AttributeError:
            # ¡Esta es la clave para tu error!
            # Esto ocurre si la instancia de UserAccount no tiene el atributo 'user' en absoluto.
            # Significa que es una instancia antigua que no fue migrada correctamente.
            return f"UserAccount (ID: {self.pk} - Datos Antiguos/Corruptos)"

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'
        ordering = ['-created_at']  # Order by creation date, newest first
        permissions = [
            ('can_view_account', 'Can view user account'),
            ('can_edit_account', 'Can edit user account'),
            ('can_delete_account', 'Can delete user account'),
        ]

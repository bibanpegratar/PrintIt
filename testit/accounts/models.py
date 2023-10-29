from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_seller = models.BooleanField(null=True)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # Add custom fields here, if needed

    def __str__(self):
        return self.email
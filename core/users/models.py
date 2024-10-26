from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.conf import settings

import uuid


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('An user needs an email to be created.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser needs is_staff set to True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser needs is_superuser set to True')
        
        return self._create_user(email, password, **extra_fields)

# personnalized User model, use 
class User(AbstractUser):
    """Personnalized User model. Use email and password to login, has an
    uuid identifier for public use."""

    username = None
    email = models.EmailField(
        verbose_name="Mail address",
        max_length=255,
        unique=True)
    
    public_id = models.UUIDField(
        verbose_name="Public identifier",
        default=uuid.uuid4,
        editable=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()



from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from operator import mod
from pyexpat import model
from statistics import mode
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.contrib.auth.hashers import make_password

from project.settings import LANGUAGE_CODE

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        username = email
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField(_('email address'), blank=True, unique=True)
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    def save(self, *args, **kwargs): 
        self.username = self.email
        return super().save(*args, **kwargs)



class Bulb(models.Model):
    bulb_statuses = (
        ('1', 'On'),
        ('0', 'Off')
    )
    status = models.CharField(choices=bulb_statuses, default='0', max_length=1)


    def __str__(self) -> str:
        return "Bulb number " + str(self.id)

from django.db import models
from utils.base_model import BaseModel
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    def create_user(self, id, email, phone_number, username, password=None):
        if not password:
            raise ValueError("Password is required")

        user = self.model(
            id=id,
            email=self.normalize_email(email),
            phone_number=phone_number,
            username=username,
        )
        try:
            password_validation.validate_password(password, user)
        except ValidationError as e:
            return None, f"Password is too weak: {', '.join(e.messages)}"

        user.set_password(password)  
        user.save()
        return user, None

    def create_superuser(self, email, username, password=None):
        user, error = self.create_user(
            id=None,
            email=email,
            phone_number="N/A", 
            username=username,
            is_superuser=True,
            password=password,
        )
        if error:
            return None, error
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user, None
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_cleaner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = AppUserManager()

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.username

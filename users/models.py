from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('Users must have a valid email address'))
        if not username:
            raise ValueError(_('Users must have a username'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **other_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            **other_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        _('email address'), 
        max_length=255, 
        unique=True
    )

    username = models.CharField(
        max_length=32, 
        unique=True
    )

    date_created = models.DateTimeField(
        verbose_name='date created', 
        auto_now_add=True
    )

    last_login = models.DateTimeField(
        verbose_name='last login', 
        auto_now=True
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

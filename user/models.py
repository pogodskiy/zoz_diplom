from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if email is None:
            email = input('Enter email: ')

        return self.create_user(username, password, email=email, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, verbose_name='Username', unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_superuser = kwargs.get('is_superuser', False)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def create_superuser(self, username, password=None, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, email=email, **extra_fields)

    @property
    def is_admin(self):
        return self.is_superuser


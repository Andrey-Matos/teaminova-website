from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None,):
        if not email:
            msg = 'Users must have an email address'
            raise ValueError(msg)

        if not username:
            msg = 'This username is not valid'
            raise ValueError(msg)

        user = self.model(email=email,username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password,date_of_birth):
        user = self.create_user(email,password=password,username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    username = models.TextField(max_length=20)
    REQUIRED_FIELDS = ["username"]

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(AbstractBaseUser):
    def create_use(self, username, email, password):
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_superuser(
            username=username,
            email=email,
            password=password
        )
        user.is_admin=True
        user.save()
        return user
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    username = models.CharField(max_length=30,unique=True,db_index=True)
    email = models.EmailField(max_length=30,unique=True,blank=True)
    group = models.ManyToManyField(to='Goup', null=True, blank=True)
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def get_username(self):
        return self.username

    def has_permission(self, permission):
        return True #TODO




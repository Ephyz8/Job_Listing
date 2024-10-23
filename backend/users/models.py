from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _ 
from .managers import CustomUserManager
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name= models.CharField(_("First Name"), max_length=150)
    last_name= models.CharField(_("Last Name"), max_length=150)
    email= models.EmailField(_("Email Adress"), max_length=254, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    def __str__(self):
        return str(self.email)
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
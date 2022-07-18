from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from decimal import Decimal
from django.utils.translation import gettext_lazy as _


class Register(models.Model):
    email = models.EmailField(_('email address'), unique=True) 
    # full_name = models.CharField(_('full_name'), max_length=200,blank=True)
    # middlename = models.CharField(_('middlename'), max_length=60, blank=True)
    # lastname = models.CharField(_('lastname'), max_length=60, blank=True)
    password = models.CharField(
        _("password"),
        max_length=128,
        help_text=_(
            "Use'[algo]$[salt]$[hexdigest]' or use the \
                < a href=\"password/\">change password form</a>."
        ),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Registers"
    
    def __str__(self):
        return self.email


class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\- ]+$'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    # last_name = models.CharField(_('last name'), max_length=50, blank=True)

    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # email = models.EmailField(_('email address'), unique=True) 
    # password = models.CharField(
    #     _("password"),
    #     max_length=128,
    #     help_text=_(
    #         "Use'[algo]$[salt]$[hexdigest]' or use the \
    #             < a href=\"password/\">change password form</a>."
    #     ),
    #     blank=True,
    #     null=True,
    # )
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    

    def __str__(self):
        return self.user.__str__()
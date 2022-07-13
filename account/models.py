from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser
# class User(AbstractUser):
#     username = models.CharField(blank=True, null=True)
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     def __str__(self):
#         return "{}".format(self.email)

class Register(models.Model):
    email = models.EmailField(_('email address'), unique=True) 
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
    user = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[MyValidator()],
            error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)

    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(_('email address'), unique=True) 
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
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    

    def __str__(self):
        return self.user.username
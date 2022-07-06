from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, blank=True)
    # firstname =  models.CharField(_("firstname"),max_length = 200)
    # middlename = models.CharField(_("middlename"),max_length = 200,blank=True, null=True)
    # lastname = models.CharField(_("lastname"),max_length = 200)
    # email = models.EmailField("email"),max_length = 200,blank=True, null=True)
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
        """Meta definition for Profile"""
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    def __str__(self):
        """Unicode representation of Profile"""
        return self.firstname

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# Creayour models here.te 

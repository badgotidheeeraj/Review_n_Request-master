from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class UserAccount(AbstractUser):
#     """
#     Customizing the User model
#     """
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     is_expert = models.BooleanField(default=False)


def no_email_validation(value):
    """
    A custom email validator that performs no validation.
    """
    pass


class UserAccount(AbstractUser):
    """
    Customizing the User model
    """
    username = models.CharField('username', max_length=100, unique=True)
    email = models.EmailField(
        'email address', unique=True, validators=[no_email_validation])
    # USERNAME_FIELD = 'email'
    full_name = models.CharField("Full Name", max_length=150)
    is_expert = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)



    # def save(self, *args, **kwargs):
    #     self.full_name = f"{self.first_name} {self.last_name}".strip()
    #     super().save(*args, **kwargs)


class UserProfile(models.Model):
    userAccount = models.OneToOneField(UserAccount, verbose_name=_("Link a User Account"), on_delete=models.CASCADE)
    about = models.TextField(verbose_name=_("About Yourself"), max_length=1000, null=True, blank=True)
    area = models.CharField(_("Area"), max_length=50, null=True, blank=True)
    domain = models.CharField(_("Domain"), max_length=50, null=True, blank=True)
    whatsApp_no = models.CharField(_("WhatsApp No"), max_length=20, null=True, blank=True)
    phone_no = models.CharField(_("Phone No"), max_length=20, null=True, blank=True)
    phone_same_as_whatsapp = models.BooleanField(_("Phone No same as WhatsApp No"), default=False, blank=True)
    email_is_verified = models.BooleanField(_("Email Verified"), default=False, blank=True)
    phone_is_verified = models.BooleanField(_("Phone Verified"), default=False, blank=True)
    whatsApp_no_is_verified = models.BooleanField(_("WhatsApp No Verified"), default=False, blank=True)
    country = models.CharField(_("Country"), max_length=50, null=True, blank=True)
    state = models.CharField(_("State"), max_length=50, null=True, blank=True)
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=500, null=True, blank=True)

    def __str__(self):
        return self.userAccount.username



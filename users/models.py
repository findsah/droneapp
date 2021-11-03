import binascii
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class customer(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email_address = models.EmailField()
    password = models.CharField(max_length=300)
    # admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:re',
                       kwargs={'id': self.id,
                               'sid': urlsafe_base64_encode(force_bytes(self.email_address))}
                       )


class controlroom(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email_address = models.EmailField()


class seller(models.Model):
    name = models.CharField(max_length=300)
    email_address = models.EmailField(null=True,blank=True,default='optional')
    location = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)


class Token(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        customer, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

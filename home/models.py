# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Abstractaddress(models.Model):

    #__Abstractaddress_FIELDS__
    active = models.BooleanField()
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    update_time = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Abstractaddress_FIELDS__END

    class Meta:
        verbose_name        = _("Abstractaddress")
        verbose_name_plural = _("Abstractaddress")


class Member(models.Model):

    #__Member_FIELDS__
    active = models.BooleanField()
    member_type = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateTimeField(blank=True, null=True, default=timezone.now)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    line_id = models.CharField(max_length=255, null=True, blank=True)
    contact_address = models.TextField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    member_uuid = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Member_FIELDS__END

    class Meta:
        verbose_name        = _("Member")
        verbose_name_plural = _("Member")


class Addressshipping(models.Model):

    #__Addressshipping_FIELDS__
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    #__Addressshipping_FIELDS__END

    class Meta:
        verbose_name        = _("Addressshipping")
        verbose_name_plural = _("Addressshipping")


class Addressbilling(models.Model):

    #__Addressbilling_FIELDS__
    tax_id = models.CharField(max_length=255, null=True, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    #__Addressbilling_FIELDS__END

    class Meta:
        verbose_name        = _("Addressbilling")
        verbose_name_plural = _("Addressbilling")



#__MODELS__END

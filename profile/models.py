from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Address (models.Model):
    ADDRESS_TYPES = (
        ('b','Billing Address'),
        ('s','Shipping Address'),
    )

    user = models.ForeignKey(User)
    addtype = models.CharField('address type', max_length=1, choices=ADDRESS_TYPES)
    addr1 = models.CharField('address line 1', max_length=100)
    addr2 = models.CharField('address line 2', max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField('zip', max_length=5)
    pub_date = models.DateTimeField('published', auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.user, self.addtype)

class Billing(models.Model):
    MONTHS = (
        ('1','January'),
        ('2','February'),
        ('3','March'),
        ('4','April'),
        ('5','May'),
        ('6','June'),
        ('7','July'),
        ('8','August'),
        ('9','September'),
        ('10','October'),
    )

    user = models.ForeignKey(User)
    description = models.CharField('card description', max_length=100)
    name = models.CharField('name on card', max_length=100)
    ccnum = models.CharField('credit card number', max_length=16)
    expirationm = models.IntegerField('expiration month', max_length=100, choices=MONTHS)
    expirationy = models.IntegerField('expiration year', max_length=100)
    ccid = models.CharField('credit card name', max_length=3)
    pub_date = models.DateTimeField('published', auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.user, self.title)

class Rating(models.Model):
    RATE = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    
    buyer = models.ForeignKey(User, related_name='Buyer')
    seller = models.ForeignKey(User, related_name='Seller')
    rating = models.PositiveSmallIntegerField(choices=RATE)
    comment = models.TextField(blank=True)
    pub_date = models.DateTimeField('published', auto_now_add=True)
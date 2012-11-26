from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from profile.models import *

class Category(models.Model):
    pid = models.ForeignKey('self', verbose_name='Parent Category')
    name = models.CharField('category name', max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Product (models.Model):
    SHIP_TYPES = (
        ('0','Local Pick-up'),
        ('1','1-day Shipping'),
        ('2','2-day Shipping'),
        ('3','Standard Shipping'),
    )

    PRODUCT_CONDITIONS = (
        ('n','New'),
        ('u','Used'),
    )

    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    code = models.CharField('product code', max_length=100, help_text='Used for easier searches.  For books, enter the ISBN; for music, enter the ISMN; for others, enter a useful code such as the UPC code.')
    title = models.CharField(max_length=50)
    description = models.TextField('description', help_text='Description of your product.  Images can be stored on a 3rd party site, such ')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField('product condition', max_length=1, choices=PRODUCT_CONDITIONS, default='u')
    shiptype = models.CharField('preferred shipping method', max_length=3, choices=SHIP_TYPES, default=0, help_text='How the product will be delivered. Default: Local Pick-up')
    shipfee = models.DecimalField('shipping fee', max_digits=10, decimal_places=2, default=0, help_text='Fee to be charged for the shipping type. Default: $0.00')
    enabled = models.BooleanField('is enabled', default=True, help_text='Determines if this product is currently listed/available.')
    expiration = models.DateTimeField('expiration date', help_text='Date the product is automatically disabled.')
    sold = models.DateTimeField('date sold')
    pub_date = models.DateTimeField('published', auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
    
    def was_published_within_day(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)
    
    def was_published_within_week(self):
        return self.pub_date >= timezone.now() - timedelta(days=7)

    def was_published_within_month(self):
        return self.pub_date >= timezone.now() - timedelta(days=30)

class Order(models.Model):
    ORDER_STATUSES = (
        ('or','Order Placed'),
        ('pr','Payment Received'),
        ('os','Order Shipped'),
        ('sr','Shipment Received'),
    )

    user = models.ForeignKey(User)
    product = models.OneToOneField(Product)
    billing = models.ForeignKey(Billing)
    status = models.CharField('preferred shipping method', max_length=2, choices=ORDER_STATUSES)
    statusinfo = models.TextField('shipping status info', blank=True, null=True)
    mod_date = models.DateTimeField('modified', auto_now=True)
    pub_date = models.DateTimeField('published', auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.user, self.id)

    def __unicode__(self):
        return "%s - %s" % (self.user, self.id)
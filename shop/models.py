from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
    addr2 = models.CharField('address line 2', max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField('zip', max_length=5)
    pub_date = models.DateTimeField('date published')

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
        ('11','November'),
        ('12','December'),
    )

    user = models.ForeignKey(User)
    desc = models.CharField('card description', max_length=100)
    name = models.CharField('name on card', max_length=100)
    ccnum = models.CharField('credit card number', max_length=16)
    expirationm = models.IntegerField('expiration month', max_length=100, choices=MONTHS)
    expirationy = models.IntegerField('expiration year', max_length=100)
    ccid = models.CharField('credit card name', max_length=3)
    pub_date = models.DateTimeField('date published')

class Category(models.Model):
    pid = models.ForeignKey('self', verbose_name='Parent Category', blank=True, null=True)
    name = models.CharField('category name', max_length=100)

class Order(models.Model):
    ORDER_STATUSES = (
        ('or','Order Placed'),
        ('pr','Payment Received'),
        ('os','Order Shipped'),
        ('sr','Shipment Received'),
    )

    user = models.ForeignKey(User)
    billing = models.ForeignKey(Billing)
    status = models.CharField('preferred shipping method', max_length=2, choices=ORDER_STATUSES)
    statusinfo = models.TextField('shipping status info')
    pub_date = models.DateTimeField('date published')

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
    order = models.OneToOneField(Order)
    code = models.CharField('product code', max_length=100, help_text='Used for easier searches.  For books, enter the ISBN; for music, enter the ISMN; for others, enter a useful code such as the UPC code.')
    title = models.CharField(max_length=50)
    desc = models.TextField('description', help_text='Description of your product.  Images can be stored on a 3rd party site, such ')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField('product condition', max_length=1, choices=PRODUCT_CONDITIONS, default='u')
    shiptype = models.CharField('preferred shipping method', max_length=3, choices=SHIP_TYPES, default=0, help_text='How the product will be delivered. Default: Local Pick-up')
    shipfee = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text='Fee to be charged for the shipping type. Default: $0.00')
    enabled = models.BooleanField('is enabled', default=True, help_text='Determines if this product is currently listed/available.')
    expiration = models.DateTimeField('expiration date', help_text='Date the product is automatically disabled.')
    sold = models.DateTimeField('date sold')
    pub_date = models.DateTimeField('date published')
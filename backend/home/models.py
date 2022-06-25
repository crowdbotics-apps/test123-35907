from django.conf import settings
from django.db import models


class AddPaymentMethodScreen(models.Model):
    "Generated Model"
    firstname = models.CharField(
        max_length=256,
    )
    lastname = models.CharField(
        max_length=256,
    )
    emailaddress = models.EmailField(
        max_length=254,
    )
    creditcardnumber = models.CharField(
        max_length=256,
    )
    ccv = models.IntegerField()
    expirationdate = models.DateField()

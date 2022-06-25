from django.conf import settings
from django.db import models


class DirectMessagesScreen6(models.Model):
    "Generated Model"
    firstname = models.CharField(
        max_length=256,
    )
    lastname = models.CharField(
        max_length=256,
    )
    dob = models.DateField()
    emailaddress = models.EmailField(
        max_length=254,
    )


# Create your models here.

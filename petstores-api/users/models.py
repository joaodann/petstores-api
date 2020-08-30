import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models


class PetStore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=8, default='')
    neighborhood = models.CharField(max_length=30, default='')
    latitude = models.CharField(max_length=12, default='')
    longitude = models.CharField(max_length=12, default='')
    species = ArrayField(models.CharField(max_length=30), blank=True)

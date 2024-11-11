import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class UploadedFile(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    file = models.FileField()
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

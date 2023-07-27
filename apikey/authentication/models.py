from django.db import models
from apikey.common.models import BaseModel
from apikey.company.models import Company

import secrets
import hashlib


class ApiKeyManager(models.Manager):
    def generate_api_key(self):
        random_string = secrets.token_urlsafe(64)
        hashed_api_key = hashlib.sha256(random_string.encode()).hexdigest()
        return hashed_api_key


class ApiKey(BaseModel):

    api_key = models.CharField(max_length=255, default=ApiKeyManager().generate_api_key, editable=False)
    company = models.ForeignKey(Company, related_name='api_keys', on_delete=models.PROTECT)

    objects = ApiKeyManager()

    def __str__(self):
        return self.api_key
from django.db import models
from apikey.common.models import BaseModel


class ApiKey(BaseModel):

    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.api_key
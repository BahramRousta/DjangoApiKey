import uuid
from django.db import models
from apikey.common.models import BaseModel
from apikey.company.models import Company


class ApiKey(BaseModel):

    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, related_name='api_key', on_delete=models.PROTECT)

    def __str__(self):
        return self.api_key

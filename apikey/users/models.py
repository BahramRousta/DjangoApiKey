from django.contrib.auth.models import AbstractUser
from apikey.common.models import BaseModel


class BaseUser(BaseModel, AbstractUser):
    pass

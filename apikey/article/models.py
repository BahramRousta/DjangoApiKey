from django.db import models
from apikey.common.models import BaseModel


class Article(BaseModel):

    title = models.CharField(max_length=255, db_index=True)
    body = models.TextField(max_length=255)

    class Meta:
        ordering = ('created_at',)
        db_table = 'article'

    def __str__(self):
        return self.title


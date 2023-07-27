from django.urls import path
from .apis import CreateApiKeyAPIView


urlpatterns = [
    path('create/', CreateApiKeyAPIView.as_view(), name='create-api-key'),
]

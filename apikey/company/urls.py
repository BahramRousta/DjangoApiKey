from django.urls import path
from .apis import CreateCompanyAPIView


urlpatterns = [
    path('company/', CreateCompanyAPIView.as_view(), name='create-company'),
]
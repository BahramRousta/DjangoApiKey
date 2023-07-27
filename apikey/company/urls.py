from django.urls import path
from .apis import CreateCompanyAPIView


urlpatterns = [
    path('create/', CreateCompanyAPIView.as_view(), name='create-company'),
]
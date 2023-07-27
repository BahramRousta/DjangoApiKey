from django.urls import path
from apikey.article.apis import CreateArticleAPIView

urlpatterns = [
    path('create/', CreateArticleAPIView.as_view(), name='create-article'),
]

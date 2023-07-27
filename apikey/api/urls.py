from django.urls import path, include

urlpatterns = [
    path('company/', include('apikey.company.urls')),
    path('api_key/', include('apikey.authentication.urls')),
    path('article/', include('apikey.article.urls')),
]

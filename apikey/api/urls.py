from django.urls import path, include

urlpatterns = [
    path('company/', include('apikey.company.urls')),
]

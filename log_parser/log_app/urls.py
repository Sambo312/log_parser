from django.urls import path
from log_app.views import index


urlpatterns = [
    path('', index),
]

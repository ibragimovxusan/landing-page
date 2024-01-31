from django.urls import path
from .views import register

urlpatterns = [
    # path('', index, name="iname"),
    path('', register),
]

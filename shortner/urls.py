from django.urls import path
from .views import index_view, redirect_to_url

urlpatterns = [
    path("", index_view, name="index"),
    path("u/<str:slug>/", redirect_to_url, name="redirect"),
]

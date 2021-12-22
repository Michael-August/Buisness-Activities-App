from django.urls import path
from .views import CollectedList

urlpatterns = [
    path('collectedList/', CollectedList.as_view(), name="collectedList")
]

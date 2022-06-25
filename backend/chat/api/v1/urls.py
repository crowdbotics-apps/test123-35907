from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DirectMessagesScreen6ViewSet

router = DefaultRouter()
router.register("directmessagesscreen6", DirectMessagesScreen6ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

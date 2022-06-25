from rest_framework import authentication
from chat.models import DirectMessagesScreen6
from .serializers import DirectMessagesScreen6Serializer
from rest_framework import viewsets


class DirectMessagesScreen6ViewSet(viewsets.ModelViewSet):
    serializer_class = DirectMessagesScreen6Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DirectMessagesScreen6.objects.all()

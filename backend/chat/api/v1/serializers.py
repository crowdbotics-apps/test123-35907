from rest_framework import serializers
from chat.models import DirectMessagesScreen6


class DirectMessagesScreen6Serializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessagesScreen6
        fields = "__all__"

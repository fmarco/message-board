from rest_framework import serializers
from .models import Message
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Message
        fields = ('author', 'message', 'date', 'image')

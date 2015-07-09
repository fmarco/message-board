from rest_framework import serializers
from .models import Message
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class MessageSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Message
        fields = ('pk', 'author', 'message', 'date', 'image')

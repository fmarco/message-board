from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from django.core.files import File
from django.core.files.base import ContentFile

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()

    @list_route(methods=['get'], permission_classes=[permissions.AllowAny])
    def all(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        from django.core.files.uploadedfile import SimpleUploadedFile

        photo_file = None
        if 'file_content' in self.request.FILES:
            photo = self.request.data['file_content'].file
            print photo
            print type(photo)
            photo_file = SimpleUploadedFile('ciai',photo)
            print photo_file
        serializer.save(
            author=self.request.user,
            message=self.request.data['message'],
            #photo=photo_file
        )

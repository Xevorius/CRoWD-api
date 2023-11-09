from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, UserSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        chat = self.get_object()
        serializer = self.serializer_class(chat)
        return Response(serializer.data)

    def update(self, request, pk=None):
        chat = self.get_object()
        serializer = self.serializer_class(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        chat = self.get_object()
        chat.delete()
        return Response(status=204)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        message = self.get_object()
        serializer = self.serializer_class(message)
        return Response(serializer.data)

    def update(self, request, pk=None):
        message = self.get_object()
        serializer = self.serializer_class(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        message = self.get_object()
        message.delete()
        return Response(status=204)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.get_object()
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response(status=204)

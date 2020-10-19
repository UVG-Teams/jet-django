from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    @action(detail=False, url_path='create_user', methods=['POST'])
    def newUser (self, request):
        usuario = User(
            username= request.data['username'],
            first_name= request.data['firstName'],
            last_name= request.data['lastName'],
            email= request.data['email']
        )
        usuario.set_password(request.data['password'])
        usuario.save()
        return Response({
            'status':'ok'
        })

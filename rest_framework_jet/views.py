from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from jetDjango.settings import GLOBAL_JET
from jet.utils import hmac_sha256


class GenerateJET(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Not active')

        payload = {
            'id': user.id
        }

        user_secret = hmac_sha256(username, password, 'ascii')
        token = GLOBAL_JET.encrypt(user_secret, payload)
        return Response({ "token": token })

class VerifyJET(APIView):

    def post(self, request, *args, **kwargs):
        payload = {}
        user_secret = hmac_sha256('user-password', 'user-password', 'ascii')
        token = GLOBAL_JET.encrypt(user_secret, payload)
        return Response(token)

class RefreshJET(APIView):

    def post(self, request, *args, **kwargs):
        payload = {}
        user_secret = hmac_sha256('user-password', 'user-password', 'ascii')
        token = GLOBAL_JET.encrypt(user_secret, payload)
        return Response(token)

generate_jet = GenerateJET.as_view()
verify_jet = VerifyJET.as_view()
refresh_jet = RefreshJET.as_view()

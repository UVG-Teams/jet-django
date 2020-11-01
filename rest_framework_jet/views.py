from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from jetDjango.settings import GLOBAL_JET
from jet.utils import hmac_sha256


class GenerateJET(APIView):

    def post(self, request, *args, **kwargs):
        payload = {}
        user_secret = hmac_sha256('user-password', 'user-password', 'ascii')
        token = GLOBAL_JET.encrypt(user_secret, payload)
        return Response(token)

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

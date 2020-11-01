from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from rest_framework import authentication, exceptions

from jetDjango.settings import GLOBAL_JET
from jet.utils import hmac_sha256
from jet.exceptions import JETException

class JETAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token(request)

        if not token:
            return None

        token = smart_str(token)
        # TODO: user secret must be calculated
        user_secret = hmac_sha256('user-password', 'user-password', 'ascii')

        try:
            decrypted_meta, decrypted_payload = GLOBAL_JET.decrypt(user_secret, token)
            print(decrypted_payload)
        except JETException:
            raise exceptions.AuthenticationFailed('Bad token')

        try:
            # TODO: get user inside payload
            user = User.objects.get(username=token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No user found')

        return (user, decrypted_payload)
    
    def get_token(self, request):
        auth_header = authentication.get_authorization_header(request)

        if not auth_header:
            return None

        if len(auth_header.split()) != 2:
            return None

        prefix, token = auth_header.split()

        if smart_str(prefix) != 'JET':
            return None

        return token

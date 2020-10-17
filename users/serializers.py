from rest_framework import serializers
from django.contrib.auth.models import User

#from tutorias.serializers import TutorSerializer
class UserSerializer(serializers.ModelSerializer):
    # tutor = TutorSerializer(many = False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedIdentityField):
    pass
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()


class CustomUserSerializer(serializers.HyperlinkedIdentityField):
    pass


class RegisterSerializer(serializers.Serializer):
    # email = serializers.EmailField(required=True, validator=[UniqueValidator])
    password_1 = serializers.CharField(required=True)
    password_2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password_1',
                  'password_2', 'firsts_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError(
                {'password': 'Passwords not same'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password_1'])
        user.save()

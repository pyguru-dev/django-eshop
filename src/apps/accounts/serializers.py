from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import (Address, Bank, City, Province,
                     OtpRequest, ActivationCode, User,
                     Wallet, UserProfile, UserMeta,)


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank


class CitySerializer(ModelSerializer):
    class Meta:
        model = City


class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province


class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile


class UserMetaSerializer(ModelSerializer):
    class Meta:
        model = UserMeta

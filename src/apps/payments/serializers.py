from rest_framework import serializers
from .models import Gateway, Payment


class GatewaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gateway
        fields = ['id', 'title', 'url']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['price', 'url']

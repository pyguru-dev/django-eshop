from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    short_address = serializers.SerializerMethodField()

    def get_short_address(self, obj):
        return

    class Meta:
        model = Url
        fields = ['url', 'slug', 'visit_count', 'created_at']

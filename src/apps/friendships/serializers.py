from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FriendshipSerialize(Serializer):
    class Meta:
        model = ''

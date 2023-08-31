from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']

    def get_avatar(self, instance):
        if hasattr(instance, 'profile') and instance.profile.avatar:
            return instance.profile.avatar.url
        return ''


class FriendshipSerialize(Serializer):
    class Meta:
        model = ''

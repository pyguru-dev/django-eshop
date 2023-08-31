from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Friendship


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = []
    actions = False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    # def has_delete_permission(self, request: HttpRequest, obj) -> bool:
    #     return False

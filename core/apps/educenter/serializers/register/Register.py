from rest_framework import serializers

from ...models import RegisterModel


class BaseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListRegisterSerializer(BaseRegisterSerializer):
    class Meta(BaseRegisterSerializer.Meta): ...


class RetrieveRegisterSerializer(BaseRegisterSerializer):
    class Meta(BaseRegisterSerializer.Meta): ...


class CreateRegisterSerializer(BaseRegisterSerializer):
    class Meta(BaseRegisterSerializer.Meta): ...

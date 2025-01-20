from rest_framework import serializers

from ...models import RoomsModel


class BaseRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListRoomsSerializer(BaseRoomsSerializer):
    class Meta(BaseRoomsSerializer.Meta): ...


class RetrieveRoomsSerializer(BaseRoomsSerializer):
    class Meta(BaseRoomsSerializer.Meta): ...


class CreateRoomsSerializer(BaseRoomsSerializer):
    class Meta(BaseRoomsSerializer.Meta): ...

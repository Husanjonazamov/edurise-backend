from rest_framework import serializers

from ...models import CourceModel


class BaseCourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourceModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCourceSerializer(BaseCourceSerializer):
    class Meta(BaseCourceSerializer.Meta): ...


class RetrieveCourceSerializer(BaseCourceSerializer):
    class Meta(BaseCourceSerializer.Meta): ...


class CreateCourceSerializer(BaseCourceSerializer):
    class Meta(BaseCourceSerializer.Meta): ...

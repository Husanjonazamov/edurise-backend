from rest_framework import serializers

from ...models import EducenterModel


class BaseEducenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducenterModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListEducenterSerializer(BaseEducenterSerializer):
    class Meta(BaseEducenterSerializer.Meta): ...


class RetrieveEducenterSerializer(BaseEducenterSerializer):
    class Meta(BaseEducenterSerializer.Meta): ...


class CreateEducenterSerializer(BaseEducenterSerializer):
    class Meta(BaseEducenterSerializer.Meta): ...

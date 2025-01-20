from rest_framework import serializers

from ...models import TeacherModel


class BaseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...


class RetrieveTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...


class CreateTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...

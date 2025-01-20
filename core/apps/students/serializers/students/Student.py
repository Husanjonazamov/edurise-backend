from rest_framework import serializers

from ...models import StudentModel


class BaseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListStudentSerializer(BaseStudentSerializer):
    class Meta(BaseStudentSerializer.Meta): ...


class RetrieveStudentSerializer(BaseStudentSerializer):
    class Meta(BaseStudentSerializer.Meta): ...


class CreateStudentSerializer(BaseStudentSerializer):
    class Meta(BaseStudentSerializer.Meta): ...

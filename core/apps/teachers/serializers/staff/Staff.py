from rest_framework import serializers

from ...models import StaffModel


class BaseStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListStaffSerializer(BaseStaffSerializer):
    class Meta(BaseStaffSerializer.Meta): ...


class RetrieveStaffSerializer(BaseStaffSerializer):
    class Meta(BaseStaffSerializer.Meta): ...


class CreateStaffSerializer(BaseStaffSerializer):
    class Meta(BaseStaffSerializer.Meta): ...

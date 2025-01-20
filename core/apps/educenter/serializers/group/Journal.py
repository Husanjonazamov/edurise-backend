from rest_framework import serializers

from ...models import JournalModel


class BaseJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListJournalSerializer(BaseJournalSerializer):
    class Meta(BaseJournalSerializer.Meta): ...


class RetrieveJournalSerializer(BaseJournalSerializer):
    class Meta(BaseJournalSerializer.Meta): ...


class CreateJournalSerializer(BaseJournalSerializer):
    class Meta(BaseJournalSerializer.Meta): ...

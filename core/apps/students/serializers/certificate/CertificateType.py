from rest_framework import serializers

from ...models import CertificatetypeModel


class BaseCertificatetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificatetypeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCertificatetypeSerializer(BaseCertificatetypeSerializer):
    class Meta(BaseCertificatetypeSerializer.Meta): ...


class RetrieveCertificatetypeSerializer(BaseCertificatetypeSerializer):
    class Meta(BaseCertificatetypeSerializer.Meta): ...


class CreateCertificatetypeSerializer(BaseCertificatetypeSerializer):
    class Meta(BaseCertificatetypeSerializer.Meta): ...

from rest_framework import serializers

from ...models import CertificateModel


class BaseCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCertificateSerializer(BaseCertificateSerializer):
    class Meta(BaseCertificateSerializer.Meta): ...


class RetrieveCertificateSerializer(BaseCertificateSerializer):
    class Meta(BaseCertificateSerializer.Meta): ...


class CreateCertificateSerializer(BaseCertificateSerializer):
    class Meta(BaseCertificateSerializer.Meta): ...

from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CertificateModel, CertificatetypeModel
from ..serializers.certificate import (
    CreateCertificateSerializer,
    CreateCertificatetypeSerializer,
    ListCertificateSerializer,
    ListCertificatetypeSerializer,
    RetrieveCertificateSerializer,
    RetrieveCertificatetypeSerializer,
)


@extend_schema(tags=["Certificate"])
class CertificateView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CertificateModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCertificateSerializer
            case "retrieve":
                return RetrieveCertificateSerializer
            case "create":
                return CreateCertificateSerializer
            case _:
                return ListCertificateSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["CertificateType"])
class CertificatetypeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CertificatetypeModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCertificatetypeSerializer
            case "retrieve":
                return RetrieveCertificatetypeSerializer
            case "create":
                return CreateCertificatetypeSerializer
            case _:
                return ListCertificatetypeSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

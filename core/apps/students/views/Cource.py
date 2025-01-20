from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CourceModel
from ..serializers.Cource import CreateCourceSerializer, ListCourceSerializer, RetrieveCourceSerializer


@extend_schema(tags=["Cource"])
class CourceView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CourceModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCourceSerializer
            case "retrieve":
                return RetrieveCourceSerializer
            case "create":
                return CreateCourceSerializer
            case _:
                return ListCourceSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

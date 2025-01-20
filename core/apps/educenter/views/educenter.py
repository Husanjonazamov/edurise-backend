from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import EducenterModel
from ..serializers.educenter import CreateEducenterSerializer, ListEducenterSerializer, RetrieveEducenterSerializer


@extend_schema(tags=["EduCenter"])
class EducenterView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = EducenterModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListEducenterSerializer
            case "retrieve":
                return RetrieveEducenterSerializer
            case "create":
                return CreateEducenterSerializer
            case _:
                return ListEducenterSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

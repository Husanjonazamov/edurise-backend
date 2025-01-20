from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import RegisterModel
from ..serializers.register import CreateRegisterSerializer, ListRegisterSerializer, RetrieveRegisterSerializer


@extend_schema(tags=["Register"])
class RegisterView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = RegisterModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListRegisterSerializer
            case "retrieve":
                return RetrieveRegisterSerializer
            case "create":
                return CreateRegisterSerializer
            case _:
                return ListRegisterSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

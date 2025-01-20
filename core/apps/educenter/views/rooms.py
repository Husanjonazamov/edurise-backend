from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import RoomsModel
from ..serializers.rooms import CreateRoomsSerializer, ListRoomsSerializer, RetrieveRoomsSerializer


@extend_schema(tags=["Rooms"])
class RoomsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = RoomsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListRoomsSerializer
            case "retrieve":
                return RetrieveRoomsSerializer
            case "create":
                return CreateRoomsSerializer
            case _:
                return ListRoomsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

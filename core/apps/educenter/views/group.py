from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import GroupModel, JournalModel
from ..serializers.group import (
    CreateGroupSerializer,
    CreateJournalSerializer,
    ListGroupSerializer,
    ListJournalSerializer,
    RetrieveGroupSerializer,
    RetrieveJournalSerializer,
)


@extend_schema(tags=["Group"])
class GroupView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = GroupModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListGroupSerializer
            case "retrieve":
                return RetrieveGroupSerializer
            case "create":
                return CreateGroupSerializer
            case _:
                return ListGroupSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["Journal"])
class JournalView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = JournalModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListJournalSerializer
            case "retrieve":
                return RetrieveJournalSerializer
            case "create":
                return CreateJournalSerializer
            case _:
                return ListJournalSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

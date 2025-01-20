from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import StaffModel, TeacherModel
from ..serializers.teacher import (
    CreateStaffSerializer,
    CreateTeacherSerializer,
    ListStaffSerializer,
    ListTeacherSerializer,
    RetrieveStaffSerializer,
    RetrieveTeacherSerializer,
)


@extend_schema(tags=["Teacher"])
class TeacherView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TeacherModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListTeacherSerializer
            case "retrieve":
                return RetrieveTeacherSerializer
            case "create":
                return CreateTeacherSerializer
            case _:
                return ListTeacherSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["Staff"])
class StaffView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = StaffModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListStaffSerializer
            case "retrieve":
                return RetrieveStaffSerializer
            case "create":
                return CreateStaffSerializer
            case _:
                return ListStaffSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

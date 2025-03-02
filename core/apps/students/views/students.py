from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import StudentModel
from ..serializers.students import CreateStudentSerializer, ListStudentSerializer, RetrieveStudentSerializer


@extend_schema(tags=["Student"])
class StudentView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = StudentModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListStudentSerializer
            case "retrieve":
                return RetrieveStudentSerializer
            case "create":
                return CreateStudentSerializer
            case _:
                return ListStudentSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

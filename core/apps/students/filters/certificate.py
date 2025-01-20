from django_filters import rest_framework as filters

from ..models import CertificateModel, CertificatetypeModel


class CertificateFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = CertificateModel
        fields = ("name",)


class CertificatetypeFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = CertificatetypeModel
        fields = ("name",)

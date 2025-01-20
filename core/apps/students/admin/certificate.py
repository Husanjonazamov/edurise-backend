from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CertificateModel, CertificateTypeModel


@admin.register(CertificateModel)
class CertificateAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CertificateTypeModel)
class CertificatetypeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

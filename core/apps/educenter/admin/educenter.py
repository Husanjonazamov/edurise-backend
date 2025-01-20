from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import EducenterModel


@admin.register(EducenterModel)
class EducenterAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

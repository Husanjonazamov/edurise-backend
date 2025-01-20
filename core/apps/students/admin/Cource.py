from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CourceModel


@admin.register(CourceModel)
class CourceAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

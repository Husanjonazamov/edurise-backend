from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import StaffModel


@admin.register(StaffModel)
class StaffAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import RoomsModel


@admin.register(RoomsModel)
class RoomsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

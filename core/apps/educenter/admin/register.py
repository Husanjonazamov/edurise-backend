from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import RegisterModel


@admin.register(RegisterModel)
class RegisterAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

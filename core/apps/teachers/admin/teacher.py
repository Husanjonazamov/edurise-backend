from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import TeacherModel


@admin.register(TeacherModel)
class TeacherAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

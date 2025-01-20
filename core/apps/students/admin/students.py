from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import StudentModel


@admin.register(StudentModel)
class StudentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

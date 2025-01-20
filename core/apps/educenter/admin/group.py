from django.contrib import admin
from unfold.admin import ModelAdmin
from ..models import GroupModel, JournalModel

from django.contrib.auth.models import Group


admin.site.unregister(Group)

@admin.register(GroupModel)
class GroupAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(JournalModel)
class JournalAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

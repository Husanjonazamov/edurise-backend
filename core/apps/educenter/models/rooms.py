from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.educenter.models import EducenterModel

class RoomsModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    educenter = models.ForeignKey(EducenterModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Rooms"
        verbose_name = _("RoomsModel")
        verbose_name_plural = _("RoomsModels")

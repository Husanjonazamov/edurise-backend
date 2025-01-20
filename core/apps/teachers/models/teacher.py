from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.educenter.models.educenter import EducenterModel


class TeacherModel(AbstractBaseModel):
    first_name = models.CharField(_("first_name"), max_length=255)
    last_name = models.CharField(_("last_name"), max_length=255)
    educenter = models.ForeignKey(EducenterModel, on_delete=models.CASCADE)
    phone = models.CharField(_("phone"), max_length=100)
    age = models.CharField(_("Teacher age"), max_length=100)

    def __str__(self):
        return self.first_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "teacher"
        verbose_name = _("TeacherModel")
        verbose_name_plural = _("TeacherModels")

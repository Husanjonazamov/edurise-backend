from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.educenter.models import EducenterModel

class CourceModel(AbstractBaseModel):
    DURATION = (
        (30, 30),
        (40, 40),
        (60, 60),
        (90, 90),
        (120, 120),
        (180, 180),
        (240, 240),
        (280, 280),
        (300, 300),
    )
    name = models.CharField(_("name"), max_length=255)
    duration = models.IntegerField(_("Darslar muddati"),choices=DURATION, default=90)
    educenter = models.ForeignKey(EducenterModel, on_delete=models.CASCADE)
    month_duration = models.IntegerField(_("Oylik Muddati"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Cource"
        verbose_name = _("CourceModel")
        verbose_name_plural = _("CourceModels")

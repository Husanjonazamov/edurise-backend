from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.educenter.models.educenter import EducenterModel


class RegisterModel(AbstractBaseModel):
    educenter = models.ForeignKey(EducenterModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.educenter.name}"
    
    
    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Register"
        verbose_name = _("RegisterModel")
        verbose_name_plural = _("RegisterModel")

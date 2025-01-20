from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class EducenterModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    logo = models.ImageField(_("Logotip"), upload_to='logo/', default='logo/default.jpg')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    parent = models.BigIntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "EduCenter"
        verbose_name = _("EducenterModel")
        verbose_name_plural = _("EducenterModels")





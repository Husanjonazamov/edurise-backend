from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.students.models.students import StudentModel
from core.apps.students.models.Cource import CourceModel
from core.apps.educenter.models.group import GroupModel



class CertificateModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="certificates")
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name="certificates")
    certificate_type = models.ForeignKey('CertificateTypeModel', on_delete=models.CASCADE, related_name="certificates")
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Certificate"
        verbose_name = _("CertificateModel")
        verbose_name_plural = _("CertificateModels")



class CertificateTypeModel(models.Model):
    name = models.CharField(max_length=255)
    template = models.FileField(upload_to="certificate_templates/")

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "CertificateType"
        verbose_name = _("CertificatetypeModel")
        verbose_name_plural = _("CertificatetypeModels")

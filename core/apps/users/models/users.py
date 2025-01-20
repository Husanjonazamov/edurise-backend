from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.educenter.models.educenter import EducenterModel


class UserModel(AbstractBaseModel):
    MALE_GENDER = "Erkak"
    FEMALE_GENDER = "Ayol"

    GENDERS = (
        (FEMALE_GENDER, FEMALE_GENDER),
        (MALE_GENDER, MALE_GENDER),
    )

    ACTIVE = "Aktiv"
    NOTACTIVE = "Aktiv emas"

    STATUS = ((ACTIVE, ACTIVE), (NOTACTIVE, NOTACTIVE))

    ROLE_SUPER_ADMIN = 1
    ROLE_ADMIN = 2
    ROLE_CEO = 3
    ROLE_ADMINISTRATOR = 4
    ROLE_MANGER = 5
    ROLE_CASHER = 6
    ROLE_TEACHER = 7

    ROLES = (
        (ROLE_SUPER_ADMIN, "SUPER_ADMIN"),
        (ROLE_ADMIN, "ADMIN"),
        (ROLE_CEO, "CEO"),
        (ROLE_ADMINISTRATOR, "ADMINISTRATOR"),
        (ROLE_MANGER, "MANGER"),
        (ROLE_CASHER, "CASHER"),
        (ROLE_TEACHER, "TEACHER"),
    )

    gender = models.CharField(
        choices=GENDERS, max_length=50, default=MALE_GENDER
    )
    birth_day = models.DateField(blank=True, null=True)
    role = models.IntegerField(choices=ROLES, default=ROLE_TEACHER)
    status = models.CharField(max_length=255, choices=STATUS, default=ACTIVE)
    educenter = models.ForeignKey(
        EducenterModel, on_delete=models.CASCADE, blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="avatar/",
        default="avatar/default.jpg",
        null=True,
        blank=True,
    )
    phone = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "User"
        verbose_name = _("UserModel")
        verbose_name_plural = _("UserModels")

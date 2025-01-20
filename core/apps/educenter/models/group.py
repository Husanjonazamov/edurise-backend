from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.students.models.Cource import CourceModel
from core.apps.educenter.models.rooms import RoomsModel
from core.apps.educenter.models.educenter import EducenterModel
from core.apps.users.models.users import UserModel
from django.utils.timezone import now


class GroupModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    ODD_DAYS = "Toq kunlar"
    EVEN_DAYS = "Juft kunlar"

    DAYS = ((ODD_DAYS, ODD_DAYS), (EVEN_DAYS, EVEN_DAYS))
    course = models.ForeignKey(CourceModel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="group_teacher")
    days = models.CharField(max_length=255, choices=DAYS)
    room = models.ForeignKey(RoomsModel, on_delete=models.CASCADE, related_name="group_room")
    starting_time = models.TimeField()
    starting_day = models.DateField()
    educenter = models.ForeignKey(EducenterModel, on_delete=models.CASCADE, related_name="group_education")
    price = models.CharField(max_length=255)
    users = models.ManyToManyField('students.StudentModel', blank=True, null=True, related_name="groups")

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Group"
        verbose_name = _("GroupModel")
        verbose_name_plural = _("GroupModels")



class JournalModel(AbstractBaseModel):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    student = models.ForeignKey('students.StudentModel', on_delete=models.CASCADE)
    educenter = models.ForeignKey(EducenterModel, on_delete=models.CASCADE, related_name="group_journal")
    date = models.DateField(default=now)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.group.name} | {self.student.first_name}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Journal"
        verbose_name = _("JournalModel")
        verbose_name_plural = _("JournalModels")

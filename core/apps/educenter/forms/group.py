from django import forms

from ..models import GroupModel, JournalModel


class GroupForm(forms.ModelForm):

    class Meta:
        model = GroupModel
        fields = "__all__"


class JournalForm(forms.ModelForm):

    class Meta:
        model = JournalModel
        fields = "__all__"

from django import forms

from ..models import GroupsModel


class GroupsForm(forms.ModelForm):

    class Meta:
        model = GroupsModel
        fields = "__all__"

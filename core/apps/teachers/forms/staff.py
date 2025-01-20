from django import forms

from ..models import StaffModel


class StaffForm(forms.ModelForm):

    class Meta:
        model = StaffModel
        fields = "__all__"

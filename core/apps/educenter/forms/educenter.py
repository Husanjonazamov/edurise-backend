from django import forms

from ..models import EducenterModel


class EducenterForm(forms.ModelForm):

    class Meta:
        model = EducenterModel
        fields = "__all__"

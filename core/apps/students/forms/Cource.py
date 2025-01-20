from django import forms

from ..models import CourceModel


class CourceForm(forms.ModelForm):

    class Meta:
        model = CourceModel
        fields = "__all__"

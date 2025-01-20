from django import forms

from ..models import RoomsModel


class RoomsForm(forms.ModelForm):

    class Meta:
        model = RoomsModel
        fields = "__all__"

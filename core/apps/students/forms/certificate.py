from django import forms

from ..models import CertificateModel, CertificatetypeModel


class CertificateForm(forms.ModelForm):

    class Meta:
        model = CertificateModel
        fields = "__all__"


class CertificatetypeForm(forms.ModelForm):

    class Meta:
        model = CertificatetypeModel
        fields = "__all__"

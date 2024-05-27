from django import forms

from esystem.models import HazardousWasteSystem


class HazardousWasteSystemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "short description of the system",
            }
        )
    )
    electronic_manifest = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    data_plus_image_manifest = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = HazardousWasteSystem
        fields = [
            "name",
            "description",
            "electronic_manifest",
            "data_plus_image_manifest",
        ]

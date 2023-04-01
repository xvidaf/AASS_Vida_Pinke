from django import forms

from EntityProvider.models import Predmet


# create a ModelForm
class TriedaForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Predmet
        fields = "__all__"

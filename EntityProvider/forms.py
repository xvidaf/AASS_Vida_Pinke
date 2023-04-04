from django import forms

from EntityProvider.models import Predmet
from EntityProvider.models import Ucitel


# create a ModelForm
class TriedaForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Predmet
        fields = "__all__"

class TeacherForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Ucitel
        fields = "__all__"

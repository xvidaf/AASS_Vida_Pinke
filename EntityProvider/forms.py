from django import forms

from EntityProvider.models import Ucitel, Predmet


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

from django.shortcuts import render

from EntityProvider.forms import TriedaForm
from EntityProvider.models import Trieda



# Create your views here.

def subjectCreation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TriedaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
    else:
        form = TriedaForm()

    return render(request, "createSubject.html", {'form': form})
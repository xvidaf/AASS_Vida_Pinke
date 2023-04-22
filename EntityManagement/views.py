import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EntityCreationLogging.views import writeToLog
from EntityProvider.forms import TriedaForm
from EntityProvider.models import Trieda

# Create your views here.
from EntityProvider.serializers import HourSerializer


def subjectCreation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TriedaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            writeToLog(request)
    else:
        form = TriedaForm()

    return render(request, "createSubject.html", {'form': form})


@csrf_exempt
def subjectCreationRest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        trieda = Trieda.objects.get(pk=data['trieda'])
        data = {'detaily': data['detaily'], 'nazov': data['nazov'], 'trieda': trieda}
        trieda = TriedaForm(data)
        if trieda.is_valid():
            trieda.save()
            return JsonResponse({"status": "200", "nazov": data["nazov"]}, safe=False)
        else:
            return JsonResponse({"status": "400"}, safe=False)



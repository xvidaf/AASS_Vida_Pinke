

from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EntityCreationLogging.models import LogPredmet
from EntityProvider.models import Trieda


@csrf_exempt
def writeToLog(request):
    log = LogPredmet(nazov_triedy=request.POST['nazov'])
    log.save()
    return HttpResponse(status=200)

@csrf_exempt
def writeToLogRest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        log = LogPredmet(nazov_triedy=data['nazov'])
        if log:
            log.save()
            return HttpResponse("Logging successful", status=200)
        else:
            return HttpResponse("Bad request", status=400)

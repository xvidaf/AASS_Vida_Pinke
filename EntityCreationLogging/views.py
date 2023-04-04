

from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from EntityProvider.models import LogPredmet

@csrf_exempt
def writeToLog(request):
    log = LogPredmet(nazov_triedy=request.POST['nazov'])
    log.save()
    return HttpResponse(status=200)
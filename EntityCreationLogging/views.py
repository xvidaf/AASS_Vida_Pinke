import pickle

import requests
from kafka import KafkaProducer
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EntityCreationLogging.models import LogPredmet

@csrf_exempt
def writeToLogRest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print("LOG Producer started")

        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
        serialized_data = pickle.dumps({"nazov": data['nazov']}, pickle.HIGHEST_PROTOCOL)
        producer.send('createLog', serialized_data)
        #requests.get('http://127.0.0.1:8000/zobrazZoznamPredmetov')
        return HttpResponse("Logging successful", status=200)
    else:
        return HttpResponse("Bad request", status=400)

@csrf_exempt
def writeToLog(request):
    log = LogPredmet(nazov_triedy=request.POST['nazov'])
    log.save()
    return HttpResponse(status=200)
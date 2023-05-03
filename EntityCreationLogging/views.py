import pickle

import requests
from confluent_kafka import Producer
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EntityCreationLogging.models import LogPredmet

@csrf_exempt
def writeToLogRest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        producer = Producer({'bootstrap.servers': 'localhost:9092'})
        print("LOG Producer started")
        serialized_data = pickle.dumps({"nazov": data['nazov']}, pickle.HIGHEST_PROTOCOL)
        producer.poll(1)
        producer.produce('NewLog', serialized_data)
        producer.flush()

        return HttpResponse("Logging successful", status=200)
    else:
        return HttpResponse("Bad request", status=400)

@csrf_exempt
def writeToLog(request):
    log = LogPredmet(nazov_triedy=request.POST['nazov'])
    log.save()
    return HttpResponse(status=200)
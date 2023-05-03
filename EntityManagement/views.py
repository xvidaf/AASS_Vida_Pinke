import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from EntityProvider.forms import TriedaForm
#from confluent_kafka import Producer
from kafka import KafkaProducer
import pickle


# Create your views here.
from EntityProvider.models import Trieda
from KafkaConsumer.views import cons
@csrf_exempt
def subjectCreationRest(request):
    if request.method == 'POST':
        cons(request)
        data = JSONParser().parse(request)
        trieda = Trieda.objects.get(pk=data['trieda'])
        data = {'detaily': data['detaily'], 'nazov': data['nazov'], 'trieda': trieda}

        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
        serialized_data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
        producer.send('NewLesson', serialized_data)

        requests.post('http://127.0.0.1:8000/log', json={"nazov": data['nazov']})

        form = TriedaForm(data)
        if form.is_valid():
            #trieda.save()
            return JsonResponse({"status": "200"}, safe=False)
    else:
        form = TriedaForm()
    return render(request, "createSubject.html", {'form': form})

def subjectCreation(request):
    if request.method == 'POST':

        #producer = Producer({'bootstrap.servers':'localhost:9092'})
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        print("1st Producer started")
        v = {
            'detaily': request.POST['detaily'],
            'nazov': request.POST['nazov'],
            'trieda': request.POST['trieda'],
        }
        serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
        producer.send('createLesson', serialized_data)

        # create a form instance and populate it with data from the request:
        form = TriedaForm(request.POST)
        # check whether it's valid:
        """if form.is_valid():
            #form.save()
            #writeToLog(request)
            pass"""

    else:
        form = TriedaForm()

    return render(request, "createSubject.html", {'form': form})

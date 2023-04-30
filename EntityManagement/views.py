from django.shortcuts import render

from EntityCreationLogging.views import writeToLog
from EntityProvider.forms import TriedaForm
from confluent_kafka import Producer
from json import loads
import json
import pickle


# Create your views here.
from KafkaConsumer.views import cons


def subjectCreation(request):
    if request.method == 'POST':

        producer = Producer({'bootstrap.servers':'localhost:9092'})
        print("Producer started")
        v = {
            'detaily': request.POST['detaily'],
            'nazov': request.POST['nazov'],
            'trieda': request.POST['trieda'],
        }
        producer.poll(1)
        producer.produce('NewLesson', v.encode('utf-8'))
        producer.flush()
        print("Data sent")

        # create a form instance and populate it with data from the request:
        form = TriedaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            #writeToLog(request)
            pass
    else:
        form = TriedaForm()

    return render(request, "createSubject.html", {'form': form})
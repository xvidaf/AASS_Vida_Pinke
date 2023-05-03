import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

#from confluent_kafka import Consumer
from kafka import KafkaConsumer
from json import loads
import json
import pickle
from threading import Thread

from EntityCreationLogging.models import LogPredmet
from EntityProvider.forms import TriedaForm
from EntityProvider.models import Trieda

#consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'earliest'})
#consumer.subscribe(['NewLesson', 'NewLog', 'LessonList'])

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print("CONSUMER STARTED")
            consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                                     api_version=(0, 10)
                                     # ,consumer_timeout_ms=1000
                                     )
            consumer.subscribe(['createLesson', 'createLog', 'listLessons'])
            for msg in consumer:
                if msg.topic:
                    print(msg.topic)
                if msg.topic == 'createLesson':
                    data = pickle.loads(msg.value)
                    form = TriedaForm(data)
                    # check whether it's valid:
                    if form.is_valid():
                        form.save()
                        print("FORM CREATED!")
                    requests.post('http://127.0.0.1:8000/log', json={"nazov": data['nazov']})
                elif msg.topic == 'createLog':
                    data = pickle.loads(msg.value)
                    log = LogPredmet(nazov_triedy=data['nazov'])
                    log.save()
                    print("LESSON CREATION LOGGED!")
                    requests.get('http://127.0.0.1:8000/zobrazZoznamPredmetov')
                elif msg.topic == 'listLessons':
                    data = pickle.loads(msg.value)
                    print(data)
                    consumer.close()
                    #return render(data['request'], 'lesson_list.html', {'predmety': data['serializer'], 'pocet_predmetov': len(data['serializer'])
                    #requests.post('http://127.0.0.1:8000/zobrazZoznamPredmetov', json={"nazov": data['nazov']})


# Create your views here.
@csrf_exempt
def cons(request):
    myClassA()
    return HttpResponse(status=200)

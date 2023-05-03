import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from confluent_kafka import Consumer
from json import loads
import json
import pickle
from threading import Thread

from EntityCreationLogging.models import LogPredmet
from EntityProvider.forms import TriedaForm
from EntityProvider.models import Trieda

consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'earliest'})
consumer.subscribe(['NewLesson', 'NewLog', 'LessonList'])

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print("CONSUMER STARTED")
            try:
                msg = consumer.poll()  # timeout
                if msg.error():
                    print('Error: {}'.format(msg.error()))
                    continue
                if msg is None:
                    continue
                if msg.topic():
                    print(msg.topic())
                if msg.topic() == 'NewLesson':
                    data = pickle.loads(msg.value())
                    form = TriedaForm(data)
                    # check whether it's valid:
                    if form.is_valid():
                        form.save()
                        print("FORM CREATED!")
                        consumer.commit()
                        requests.post('http://127.0.0.1:8000/log', json={"nazov": data['nazov']})
                elif msg.topic() == 'NewLog':
                    data = pickle.loads(msg.value())
                    log = LogPredmet(nazov_triedy=data['nazov'])
                    log.save()
                    print("LESSON CREATION LOGGED!")
                    consumer.commit()
                    requests.get('http://127.0.0.1:8000/zobrazZoznamPredmetov')
                elif msg.topic() == 'LessonList':
                    data = pickle.loads(msg.value())
                    consumer.commit()
                    requests.post('http://127.0.0.1:8000/zobrazZoznamPredmetov', json={"nazov": data['nazov']})
            except:
                print("Unexpected error")

        consumer.close()

# Create your views here.
@csrf_exempt
def cons(request):
    myClassA()
    return HttpResponse(status=200)

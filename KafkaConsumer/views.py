from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from confluent_kafka import Consumer
from json import loads
import json
import pickle
from threading import Thread

consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'earliest'})
consumer.subscribe(['NewLesson'])

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            msg = consumer.poll(1.0)  # timeout
            if msg is None:
                continue
            if msg.error():
                print('Error: {}'.format(msg.error()))
                continue
            data = msg.value().decode('utf-8')
            print(data)


# Create your views here.
@csrf_exempt
def cons(request):
    myClassA()
    return HttpResponse(status=200)

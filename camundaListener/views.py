import time
from ast import literal_eval

import requests
from django.http import HttpResponse
from django.shortcuts import render
import pycamunda.externaltask
from rest_framework.parsers import JSONParser

subjectToCreate = {"detaily": "predmet o slovenskom jazyku",
    "nazov": "Slovencina",
    "trieda": "1"}

# Create your views here.

def camundaProces(request):
    print("Sme tu")
    url = 'http://localhost:8080/engine-rest'
    worker_id = 'my-worker'
    variables = ['detaily', 'nazov', 'trieda', 'id_predmetu']  # variables of the process instance
    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='vytvorPredmet', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        subjectToCreate = {"detaily": task.variables['detaily'].value,
                           "nazov": task.variables['nazov'].value,
                           "trieda": task.variables['trieda'].value}

        status = requests.post('http://127.0.0.1:8000/createSubjectRest', json=subjectToCreate)
        status = literal_eval(status.content.decode('utf-8'))
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='vytvorPredmet', value=status['status'])  # Send this variable to the instance
        print(status)
        complete()

    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='zalogujVytvorenie', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        status = requests.post('http://127.0.0.1:8000/log', json={"nazov": subjectToCreate['nazov']})
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='zalogujVytvorenie', value=str(status.status_code))  # Send this variable to the instance
        print(status.status_code)
        complete()

    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='zobrazZoznam', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        lessons = requests.get('http://127.0.0.1:8000/hours').json()
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='zobrazZoznam', value=lessons)  # Send this variable to the instance
        print(lessons)
        complete()

    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='zobrazDetail', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        lesson = requests.get('http://127.0.0.1:8000/zobrazPredmet/{}'.format(task.variables['id_predmetu'].value)).json()
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='zobrazDetail', value=lesson)  # Send this variable to the instance
        print(lesson)
        complete()

    return HttpResponse("Camunda process DONE", status=200)

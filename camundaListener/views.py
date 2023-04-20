import time

from django.http import HttpResponse
from django.shortcuts import render
import pycamunda.externaltask



# Create your views here.

def camundaProces(request):
    print("Sme tu")
    url = 'http://localhost:8080/engine-rest'
    worker_id = 'my-worker'
    variables = ['InitVariable']  # variables of the process instance
    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='vytvorPredmet', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        time.sleep(3)
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='vytvorPredmet', value="DONE")  # Send this variable to the instance
        complete()

    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='zalogujVytvorenie', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        time.sleep(3)
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='zalogujVytvorenie', value="DONE")  # Send this variable to the instance
        complete()

    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='zobrazZoznam', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        time.sleep(3)
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='zobrazZoznam', value="DONE")  # Send this variable to the instance
        complete()

    fetch_and_lock = pycamunda.externaltask.FetchAndLock(url=url, worker_id=worker_id, max_tasks=1)
    fetch_and_lock.add_topic(name='zobrazDetail', lock_duration=10000, variables=variables)
    tasks = fetch_and_lock()

    for task in tasks:
        time.sleep(3)
        complete = pycamunda.externaltask.Complete(url=url, id_=task.id_, worker_id=worker_id)
        complete.add_variable(name='zobrazDetail', value="DONE")  # Send this variable to the instance
        complete()

    return HttpResponse(status=200)
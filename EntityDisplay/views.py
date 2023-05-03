import pickle

from confluent_kafka import Producer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.core import serializers



#View of hour table
from django.views.decorators.csrf import csrf_exempt
from rest_framework.templatetags.rest_framework import data

from EntityProvider.models import Predmet
from EntityProvider.urls import HourSerializer
from KafkaConsumer.views import cons

@csrf_exempt
def zobrazZoznamPredmetovRest(request):
    if request.method == 'GET':
        lessons = Predmet.objects.all()
        serializer = HourSerializer(lessons, many=True)
        producer = Producer({'bootstrap.servers': 'localhost:9092'})
        print("LESSON LIST Producer started")
        serialized_data = pickle.dumps(serializer, pickle.HIGHEST_PROTOCOL)
        producer.poll(1)
        producer.produce('LessonList', serialized_data)
        producer.flush()
        return HttpResponse(200)
    elif request.method == 'POST':
        print(request.POST)
        return render(request, 'lesson_list.html', {'predmety': serializer.data, 'pocet_predmetov': len(serializer.data)})

@csrf_exempt
def zobrazPredmetRest(request, lesson_id):
    if request.method == 'GET':
        lessons = Predmet.objects.all()
        serializer = HourSerializer(lessons, many=True)
        for ser in serializer.data:
            if ser['id'] == lesson_id:
                return JsonResponse(ser, safe=False)

def zobrazZoznamPredmetov(request):
    vsetky_predmety = Predmet.objects.all().order_by('id')

    cons(request)

    if request.method == "GET":
        page = request.GET.get('page', 1)
        paginator = Paginator(vsetky_predmety, 50)
        #pocet_predmetov = vsetky_predmety.count()
        pocet_predmetov = 2
        try:
            predmety = paginator.page(page)
        except PageNotAnInteger:
            #cats = paginator.page(1)
            return redirect(request.META.get('HTTP_REFERER'))
        except EmptyPage:
            predmety = paginator.page(paginator.num_pages)

        # SOAP request URL
        url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

        # structured XML
        payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
                    <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                        <soap:Body>
                            <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                                <sCountryISOCode>SK</sCountryISOCode>
                            </CountryIntPhoneCode>
                        </soap:Body>
                    </soap:Envelope>"""
        # headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8'
        }
        # POST request
        response = requests.request("POST", url, headers=headers, data=payload)

        # prints the response
        Bs_data = BeautifulSoup(response.text, "xml")
        b_unique = Bs_data.find('m:CountryIntPhoneCodeResult')

        return render(request, 'lesson_list.html', {'predmety': predmety, 'pocet_predmetov': pocet_predmetov, 'soap': b_unique.get_text(strip = True)})
    else:
        return redirect(request.META.get('HTTP_REFERER'))


#View of teacher table
def teacher_list(request):
    cat_all = Hodina.objects.all().order_by('id')
    if request.method == "GET":
        page = request.GET.get('page', 1)
        paginator = Paginator(cat_all, 50)
        cat_count = cat_all.count()
        try:
            cats = paginator.page(page)
        except PageNotAnInteger:
            #cats = paginator.page(1)
            return redirect(request.META.get('HTTP_REFERER'))
        except EmptyPage:
            cats = paginator.page(paginator.num_pages)

        return render(request, 'teacher_list.html', {'cats': cats, 'cat_count': cat_count})
    else:
        return redirect(request.META.get('HTTP_REFERER'))

#View of lesson table
def lesson_list(request):
    vsetky_predmety = requests.get('http://localhost:8000/hours')
    vsetky_predmety = Hodina.objects.all().order_by('id')
    if request.method == "GET":
        page = request.GET.get('page', 1)
        paginator = Paginator(cat_all, 50)
        cat_count = cat_all.count()
        try:
            cats = paginator.page(page)
        except PageNotAnInteger:
            #cats = paginator.page(1)
            return redirect(request.META.get('HTTP_REFERER'))
        except EmptyPage:
            cats = paginator.page(paginator.num_pages)

        return render(request, 'lesson_list.html', {'cats': cats, 'cat_count': cat_count})
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def findParent(parent_id):
    return HttpResponse("Hello, world. You're at the polls index.")

#View hour detail
def hour(request, predmet_id):
    predmet = Predmet.objects.get(pk=predmet_id)
    return render(request, 'hour.html', {'predmet': predmet})

def cat_info_list(request):
    return HttpResponse("Hello, world. You're at the polls index.")

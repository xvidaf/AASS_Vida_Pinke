from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
# Create your views here.

from django.http import HttpResponse



#View of hour table
from EntityManagement.models import Predmet


def zobrazZoznamPredmetov(request):
    vsetky_predmety = Predmet.objects.all().order_by('id')
    if request.method == "GET":
        page = request.GET.get('page', 1)
        paginator = Paginator(vsetky_predmety, 50)
        pocet_predmetov = vsetky_predmety.count()
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

from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    TEDO=Topicforms()
    d={'TEDO':TEDO}
    if request.method=='POST':
        TDEO=Topicforms(request.POST)
        if TDEO.is_valid():
            TN=TDEO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=TN)[0]
            TO.save()
            return HttpResponse('Topic create successfully')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WDRO=Webpageforms()
    d={'WDRO':WDRO}
    if request.method=='POST':
        WDEO=Webpageforms(request.POST)
        if WDEO.is_valid():
            TN=WDEO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=TN)
            na=WDEO.cleaned_data['name']
            ur=WDEO.cleaned_data['url']
            em=WDEO.cleaned_data['email']

            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()
            return HttpResponse('Webpage create successfully')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AREO=Accessrecordforms()
    d={'AREO':AREO}
    if request.method=='POST':
        ARED=Accessrecordforms(request.POST)
        if ARED.is_valid():
            
            NA=ARED.cleaned_data['name']
            WO=Webpage.objects.get(name=NA)
            da=ARED.cleaned_data['date']
            au=ARED.cleaned_data['author']

            AO=AccessRecord.objects.get_or_create(name=WO,date=da,author=au)[0]
            AO.save()
            return HttpResponse('Access record create successfully')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_access.html',d)
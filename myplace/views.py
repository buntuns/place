from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Place , Type


def index(request):
    image = Place.objects.all()
    the_type = Type.objects.all()
    return render(request,'myplace/index.html',{'image':image,'the_type':the_type})

def details(request , select_id):
    picture = get_object_or_404(Place, pk=select_id)
    the_type = Type.objects.all()
    data1 = "myplace/static/myplace/" + str(picture.place_name) + "/p1.txt"
    data2 = "myplace/static/myplace/" + str(picture.place_name) + "/p2.txt"
    data3 = "myplace/static/myplace/" + str(picture.place_name) + "/p3.txt"
    block1  = open(data1, "r").read()
    block2  = open(data2, "r").read()
    block3  = open(data3, "r").read()
    return render(request,'myplace/details.html',{'picture':picture, 'block1':block1, 'block2':block2, 'block3':block3,'the_type':the_type})

def catalog(request):
    image = Place.objects.all()
    the_type = Type.objects.all()
    return render(request,'myplace/catalog.html',{'image':image,'the_type':the_type})

def thefilter(request, typenaja):
    image = Place.objects.filter(place_type=typenaja)
    the_type = Type.objects.all()
    
    return render(request,'myplace/catalog.html',{'image':image,'the_type':the_type})

def about(request):
    the_type = Type.objects.all()
    return render(request,'myplace/about.html',{'the_type':the_type}) 


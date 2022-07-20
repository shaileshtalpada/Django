
from ssl import VERIFY_CRL_CHECK_LEAF
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(request,'index.html')

def  about(request):
    return render(request,'about.html')

def  sportss(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=sports"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'sports.html',records)

def  fashion(request):
    return render(request,'fashion.html')





def  entr(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=entertainment"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'entr.html',records)

def  nati(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=national"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'national.html',records)

def  poli(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=politics"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'politics.html',records)


def  wor(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=world"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'world.html',records)
    
def  tech(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=technology"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'technology.html',records)
    
def  bus(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=business"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'bus.html',records)
    
def  start(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=startup"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'startup.html',records)
    
def  misce(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=miscellaneous"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'miscellaneous.html',records)
    
def  hatke(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=hatke"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'hatke.html',records)
    
def  auto(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=Automoblie"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'automoblie.html',records)

def  sci(request):
    records={}
    url="https://inshortsapi.vercel.app/news?category=science"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']= inshorts_data
    return render(request,'science.html',records)
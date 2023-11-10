from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
def add(request):
    urls=requests.get("http://www.google.com")
    beautysoup=BeautifulSoup(urls.text,'html.parser')
    address=[]
    for link in beautysoup.find_all('a'):
        address.append(link.get('href'))
    return render(request,'home.html',{'address':address})

    
    
   
        

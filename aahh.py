#Alguses impordin requests, json, BeautifulSoup ja Re
import requests
import json
from bs4 import BeautifulSoup
import re

#toome firefox'i programi
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

#ühendame veebilehe
base_url = "http://192.168.22.172/menu-example/"

#taotleme veebilehelt infot
r = requests.get(base_url,headers=header)

if r.status_code == 200:
    #loeb veebilehelt infot
    soup = BeautifulSoup(r.text, 'html.parser')
    #leiab klassi
    books = soup.find_all('div',attrs={"class":"panel panel-default"})
    #teeme result'i tuhja dictionary
    result=[]
    #teeme for loopi ja leiab kõik järgimed spetsiifilist infot
    for book in books:
        nimetus1 = book.find('h3').text
        print(nimetus1)
        toidud = book.contents[2].h2.contents[0]
        hind = book.contents[2].span.contents[0]
        lisainfo = book.find('small').text
        nimetus = book.find('h2').text
        #ühendab leitud info tähendustega
        single ={'nimetus':nimetus1,'toidud':[{'nimetus':toidud, 'hind':hind.replace("€", ""), 'lisainfo':lisainfo }], }
        result.append(single)
        #kirjutab kõik selle info Json faili
        with open('söögimenüü.json','w', encoding="UTF-8") as f:
            json.dump(result,f,indent=4)
else:
  print(r.status_code)

import requests
import json
from bs4 import BeautifulSoup
import re

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

base_url = "http://192.168.22.172/menu-example/"

r = requests.get(base_url,headers=header)




if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    books = soup.find_all('div',attrs={"class":"panel panel-default"})
    result=[]
    
    for book in books:
        nimetus1 = book.find('h3').text
        print(nimetus1)
        toidud = book.contents[2].h2.contents[0]
        hind = book.contents[2].span.contents[0]
        lisainfo = book.find('small').text
        nimetus = book.find('h2').text
        single ={'nimetus':nimetus1,'toidud':["nimetus: "+ toidud, "hind: "+ hind, "lisainfo: "+ lisainfo ], }
        result.append(single)
    with open('söögimenüü.json','w', encoding="UTF-8") as f:
        json.dump(result,f,indent=4)
else:
  print(r.status_code)
  
  


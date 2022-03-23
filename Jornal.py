import requests
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/'
r = requests.get(url)
url2 = 'https://weather.com/pt-BR/clima/hoje/l/S%C3%A3o+Paulo+S%C3%A3o+Paulo?canonicalCityId=d7593e91d7e1447404d3a75fc1f7e0513bfcc5bdd74b81f6b4299f68b5689392'
b = requests.get(url2)
soup = BeautifulSoup(b.text, 'html.parser')
week3 = soup.find(class_='h4 today_nowcard-location')
week4 = soup.find(class_='today_nowcard-temp')
soup = BeautifulSoup(r.text, 'html.parser')
week1 = soup.find(class_='chapeu color1')
week = soup.find('h1',class_='titulo color2')
e = soup.find('h2',class_='titulo color2')
site2 = 'https://www.terra.com.br/'
sitezin = requests.get(site2)
t = BeautifulSoup(sitezin.text, 'html.parser')
mainurl = t.find('a',class_='main-url text')
noti = t.find('a',class_='text item-premium')


print("Notícias do Caiao")


cont = 0
for a in soup.find_all('ul',class_='relacionadas relacionadas-simples'):
    x = a.text.split("      ")
    cont += 1
    if cont == 1:
        break
    
print(f'Cabeçalho: {week1.text}')
print(f'Noticia: {week.text}')
print(f'Noticia: {mainurl.text}')
print(f'Noticia: {noti.text}')
print(f'{e.text.lstrip(" ")}')
print("")
for i in range(0,len(x)):
    print(x[i].lstrip(" "))

print("")

print("########Temperatura###########")
print(week3.text)
print(week4.text)
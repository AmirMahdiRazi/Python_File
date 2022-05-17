import re
import requests
from bs4 import BeautifulSoup
r = requests.get("https://bama.ir/car/all-brands/all-models/all-trims?price=30-40")
soup=BeautifulSoup(r.text,"html.parser")
r=soup.find('h2',attrs={'itemprop':'name'})
print(r.text)
re.sub(r'\s+',' ',r.text)
re.sub(r'\s+',' ',r.text).strip()

all_cars = soup.find_all('h2',attrs={'itemprop' : 'name'})
for car in all_cars:
    print(re.sub(r'\s+',' ',car.text).strip())


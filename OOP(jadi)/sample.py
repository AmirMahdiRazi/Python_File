import re
import requests
from bs4 import BeautifulSoup
import mysql.connector


result1=[]

r = requests.get("https://www.truecar.com/used-cars-for-sale/listings/?page=2&sort[]=best_match" )
soup=BeautifulSoup(r.text,"html.parser")
name_car = soup.find('span',attrs={'class' : 'vehicle-header-make-model text-truncate'})
print(name_car)
print(name_car.text)

"""for name in name_car:
    result1=re.sub(r'\s+',' ',name.text).strip()
    print(result1)
"""



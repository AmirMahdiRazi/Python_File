import re
import requests
from bs4 import BeautifulSoup
r = requests.get("https://divar.ir/s/tehran")
soup=BeautifulSoup(r.text,"html.parser")
r=soup.find('div',attrs={'class':'kt-post-card__description'})
y=soup.find('div',attrs={'class':'kt-post-card__title'})
li_desc=[]
li_name=[]
count=0

desc_aghahi = soup.find_all('div',attrs={'class':'kt-post-card__description'})
name_aghahi = soup.find_all('div',attrs={'class':'kt-post-card__title'})

print(desc_aghahi[1])


for desc in desc_aghahi:
    result1=re.sub(r'\s+',' ',desc.text).strip()
    li_desc.append(result1)

for name in name_aghahi:
    result1=re.sub(r'\s+',' ',name.text).strip()
    li_name.append(result1)

if len(li_name) == len(li_desc):
    count=len(li_desc)
else:
    count = len(li_desc)

for i in range(count):
    str1=li_desc[i]
    x = str1.find("توافقی")
    if x >= 0:
        print(li_name[i])

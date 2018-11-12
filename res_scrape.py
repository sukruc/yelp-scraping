import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

cities = pd.read_csv("cities.csv")
biz_names = []
biz_street = []
biz_city = []
biz_zip = []
biz_contact = []
# s = requests.Session() # if you'd like to use a session, uncomment this line and replace requests in line 18 with session name
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
for city in cities.name.values:
    print(city)
    for page_num in range(0,500,10):
        q_url = "https://www.yelp.com/search?find_desc=restaurants&find_loc=%s&start=%d"%(city,page_num)
        r = requests.get(url=q_url,headers=headers)
        soup = BeautifulSoup(r.content,"html.parser")
        biz_all = soup.find_all("a", attrs={"class":"biz-name js-analytics-click"})
        print("businesses found: ",len(biz_all))
        if len(biz_all) == 0:
            break
        for biz_num in range(len(biz_all)):
            biz_name = soup.find_all("a", attrs={"class":"biz-name js-analytics-click"})[biz_num].find("span")
            biz_names.append(biz_name.text)
            biz_addr = soup.find_all("div", attrs={"class":"secondary-attributes"})[biz_num].find("address")
            if biz_addr is not None and len(biz_addr.contents) == 3:
                biz_street.append(biz_addr.contents[0].lstrip())
                biz_city.append(biz_addr.contents[2].rstrip().split()[0].strip(","))
                biz_zip.append(biz_addr.contents[2].rstrip().split()[2])
            elif biz_addr is not None and len(biz_addr.contents) != 3:
                biz_street.append(biz_addr.text.strip())
                biz_city.append(None)
                biz_zip.append(None)
            else:
                biz_street.append(None)
                biz_city.append(None)
                biz_zip.append(None)
            biz_phone = soup.find_all("span", attrs={"class":"biz-phone"})
            if biz_num <= len(biz_phone)-1:
                biz_contact.append(biz_phone[biz_num].text.strip())
            else:
                biz_contact.append(None)
res = pd.DataFrame(data={"name":biz_names,"address":biz_street,"city":biz_city,"zip":biz_zip})
res.drop_duplicates().to_csv("restaurants.csv",index=False)


import re
import os
import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
}  
url=input("请输入网址", )
response=requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
list_con_dd = soup.find('div', id="list")
novel_list = list_con_dd.find_all('a')
real_list = novel_list[5:9]
for real in real_list:
    href = 'http://www.maydayfans.com/'+real.get('href')
    name = real.text
    print(name)
    response = requests.request("GET", href, headers=headers) 
    response.encoding = response.apparent_encoding 
    soup2 = BeautifulSoup(response.text, 'lxml')
    bf = soup2.find('div', id="chaptercontent", class_="content")
    s=str(bf)
    s=s.replace("<br/>", '\n');
    a = re.sub(u"<.*?\\>", "", s)
    a = "".join([b for b in a.splitlines(True) if b.strip()]) 
    f = open('测试.txt',mode='a',encoding='utf-8')
    f.write(name+str(a))  
    f.close()   
   

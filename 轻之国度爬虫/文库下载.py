import os
import requests
import time
from bs4 import BeautifulSoup
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Referer': 'https://www.oh100.com/'}
base_web = 'https://www.oh100.com/kaoshi/peixun/206013.html'
response = requests.get(base_web, headers=header)
response.encoding = response.apparent_encoding
txt = response.text
soup = BeautifulSoup(txt, "lxml")#lxml用pip获取
bf=soup.find('div', class_="content")
text_ = bf.text.replace(' ', '')
text_ = "".join([s for s in text_.splitlines(True) if s.strip()])
print(text_)
f = open('name.txt' ,mode='a', encoding='utf-8')
f.write(str(text_))  # write 写入
f.close()

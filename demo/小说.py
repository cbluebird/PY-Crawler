
import re
import os
import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
}  # 构造请求头
url='http://www.dangxiaoshuo.com/conghongyuekaishi/'
response=requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#查找
list_con_dd = soup.find('dl')
#print(list_con_dd)
novel_list = list_con_dd.find_all('a')
#print(len(novel_list))
real_list = novel_list[0:2]

for real in real_list:
    href = 'http://www.dangxiaoshuo.com/'+real.get('href')
    name = real.text
    print(name)
    response = requests.request("GET", href, headers=headers) # 获取网页数据
    response.encoding = response.apparent_encoding # 当获取的网页有乱码时加
    soup2 = BeautifulSoup(response.text, 'lxml')
    bf = soup2.find('div', id="content", class_="showtxt")
    text_ = bf.text.replace(' ', '')
    text_ = name+'\n'+text_+'\n'
    text_ = "".join([s for s in text_.splitlines(True) if s.strip()])
    f = open('小说.txt' ,mode='a', encoding='utf-8')
    f.write(str(text_))  # write 写入
    f.close()
#print(chapter_names)
#print(chapter_urls)

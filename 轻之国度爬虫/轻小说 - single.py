import os
import requests
import time
from bs4 import BeautifulSoup
# coding=utf-8
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Referer': 'https://www.lightnovel.us/'}
idx = 1
base_web = 'https://www.lightnovel.us/cn/detail/825925' 
response = requests.get(base_web, headers=header)
txt = response.text
soup = BeautifulSoup(txt, "lxml")#lxml用pip获取
article = soup.find('article', id='article-main-contents')#修改图片所属
img = article.find_all('img')
save_path = 'C:/Users/win10/Desktop/轻小说python/' + str(1)#这个t代表图片文件夹名
if not os.path.exists(save_path):
    os.mkdir(save_path)
for url in img:
    resp = requests.get(url.attrs['src'], headers=header)
    print(resp.status_code)
    open(save_path + '/' + str(idx) + '.jpg', 'wb').write(resp.content) # 将内容写入图片
    idx += 1
idx += 1
#章节名称
chapter_names = []
#章节链接
chapter_urls = []
title=soup.find('h2', class_="article-title")
name=title.text
print(name)
response.encoding = response.apparent_encoding # 当获取的网页有乱码时加
bf = soup.find('article' ,id="article-main-contents")#修改文字所属
text_ = bf.text.replace(' ', '')
text_ = name+text_
text_ = "".join([s for s in text_.splitlines(True) if s.strip()])
print(text_)
f = open('name.txt' ,mode='a', encoding='utf-8')
f.write(str(text_))  # write 写入
f.close()





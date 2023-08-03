import os
import requests
import time
from bs4 import BeautifulSoup
# coding=utf-8
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Referer': 'https://www.lightnovel.us/'}
t = 1
for i in range(1047981, 1090350):
    idx = 1
    # try:
    base_web = 'https://www.lightnovel.us/cn/detail/' + str(i)
    response = requests.get(base_web, headers=header)
    txt = response.text

    if '辉夜汉化组' and '辉夜大小姐想让我告白' in txt:
        soup = BeautifulSoup(txt, "html.parser")
        article = soup.find('article', id='article-main-contents')
        img = article.find_all('img')
        save_path = 'C:/Users/wadde/Desktop/img/' + str(t)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for url in img:
            resp = requests.get(url.attrs['src'], headers=header)
            print(resp.status_code)
            open(save_path + '/' + str(idx) + '.jpg', 'wb').write(resp.content) # 将内容写入图片
            idx += 1
        idx += 1
        t = t + 1
    # except:
    #     print('something wrong')





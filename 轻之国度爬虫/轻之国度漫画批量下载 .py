import os
import requests
import time
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver #pip install selenium
# coding=utf-8
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Referer': 'https://www.lightnovel.us/'}
import selenium.webdriver as webdriver #pip install selenium
dr = webdriver.Chrome('chromedriver.exe') #https://pypi.org/project/selenium/
dr.get('https://www.lightnovel.us/cn/series/700')
buttons=dr.find_element_by_class_name('item-container').find_elements_by_class_name('item-box')
time.sleep(5)
url_list=[]
for btn in buttons:
    btn.click()
    all_window = dr.window_handles
    dr.switch_to.window(all_window[1]) # 切换到新打开的窗口
    url=dr.current_url # 获取新打开的窗口的url
    dr.close() # 关闭新打开的窗口
    dr.switch_to.window(all_window[0]) # 切换回原来的窗口
    url_list.append(url)
dr.close()
print(url_list)
t = 1
for base_web in url_list[0:47]:
    idx = 1
    print(base_web)
    response = requests.get(base_web, headers=header)
    response.encoding = response.apparent_encoding
    txt = response.text
    soup = BeautifulSoup(txt, "lxml")#lxml用pip获取
    article = soup.find('article', id='article-main-contents')#修改图片所属
    img = article.find_all('img')
    save_path = 'C:/Users/win10/Desktop/我家女友' + str(t)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for url in img:
        resp = requests.get(url.attrs['src'], headers=header)
        print(resp.status_code)
        open(save_path + '/' + str(idx) + '.jpg', 'wb').write(resp.content) # 将内容写入图片
        idx += 1
    idx += 1
    t = t + 1
    title=soup.find('h2', class_="article-title")
    name=title.text
    print(name)
    




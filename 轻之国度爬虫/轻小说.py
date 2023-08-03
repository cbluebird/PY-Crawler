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
dr.get('https://www.lightnovel.us/cn/series/660')
buttons=dr.find_element_by_class_name('item-container').find_elements_by_class_name('item-box')
time.sleep(5)
url_list=[]
for btn in buttons:
    btn.click()
    # url=dr.getCurrentUrl()

    all_window = dr.window_handles
    
    dr.switch_to.window(all_window[1]) # 切换到新打开的窗口

    url=dr.current_url # 获取新打开的窗口的url

    dr.close() # 关闭新打开的窗口

    dr.switch_to.window(all_window[0]) # 切换回原来的窗口

    url_list.append(url)

dr.close()
print(url_list)

t = 1
for base_web in url_list[0:10]:#修改范围
    idx = 1
    # try:
    print(base_web)
    response = requests.get(base_web, headers=header)
    txt = response.text
    
    if '[鴨志田一]青春豬頭少年' and '[台/繁]' in txt:#修改特征
        soup = BeautifulSoup(txt, "lxml")#lxml用pip获取
        article = soup.find('article', id='article-main-contents')#修改图片所属
        img = article.find_all('img')
        save_path = 'C:/Users/win10/Desktop/轻小说python/' + str(t)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for url in img:
            resp = requests.get(url.attrs['src'], headers=header)
            print(resp.status_code)
            open(save_path + '/' + str(idx) + '.jpg', 'wb').write(resp.content) # 将内容写入图片
            idx += 1
        idx += 1
        t = t + 1
        #章节名称
        chapter_names = []
#章节链接
        chapter_urls = []
        title=soup.find('h2', class_="article-title")
        name=title.text
        response.encoding = response.apparent_encoding # 当获取的网页有乱码时加
        #bf = soup.find('article' ,id="article-main-contents") 修改文字所属，假如文字和图片所属不一样时使用，下面article改成bf
        text_ = article.text.replace(' ', '')
        text_ = name+text_
        text_ = "".join([s for s in text_.splitlines(True) if s.strip()])
        print(text_)
        f = open('name.txt' ,mode='a', encoding='utf-8')
        f.write(str(text_))  # write 写入
        f.close()
    # except:
    #     print('something wrong')





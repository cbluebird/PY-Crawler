import os
import requests
import time
from bs4 import BeautifulSoup
# coding=utf-8
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Referer': 'https://www.lightnovel.us/'}


url = input('输入系列网址',)
response = requests.request("GET", url, headers=header) # 获取网页数据
response.encoding = response.apparent_encoding # 当获取的网页有乱码时加
soup = BeautifulSoup(response.text, 'html.parser')
bf = soup.find_all('script')
print(bf)

s = str(bf)
i=1
u=1
a_list=[]

for i in range(1,10000):
    a = s.find('aid',u)
    u=int(a)+1
    if (int(a)!=-1):
        a_list.append(a)
    else:
        break


url_list=[]
nums = []

for index in range(len(a_list)):
    line=a_list[index]
    p=''
    print(line)   
    for j in range(100):
        if(s[line+4+j]<='9' and s[line+4+j]>='0'):p=p+s[line+4+j]
        else: break
    print(p)   
    if p!='':
        nums.append(int(p))
    if(line==-1):break

nums.sort()
#print(nums)


for p in nums:
    url_list.append('https://www.lightnovel.us/cn/detail/'+str(p))

#print(url_list)


t = 1
feature1 = input('输入特征1',)
feature2 = input('输入特征2',)
for base_web in url_list:#修改范围
    idx = 1
    # try:
    response = requests.get(base_web, headers=header)
    txt = response.text

    if feature1 and  feature2 in txt:#修改特征
        soup = BeautifulSoup(txt, "lxml")#lxml用pip获取
        article = soup.find('article', id='article-main-contents')#修改图片所属
        img = article.find_all('img')
        save_path = 'D:/files' + str(t)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for url in img:
            resp = requests.get(url.attrs['src'], headers=header)
            print(resp.status_code)
            open(save_path + '/' + str(idx) + '.jpg', 'wb').write(resp.content) # 将内容写入图片
            idx += 1
        idx += 1
        t = t + 1


        response.encoding = response.apparent_encoding # 当获取的网页有乱码时加
        text_ = article.text.replace(' ', '')
        print(text_)
        f = open('name.txt' ,mode='a', encoding='utf-8')
        f.write(str(text_))  # write 写入
        f.close()
    # except:
    #     print('something wrong')





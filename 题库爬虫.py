import os
import requests

header = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Referer': 'https://www.lightnovel.us/'}
url_list = []

url = 'https://max.book118.com/html/2022/0529/8027026061004104.shtm'
response = requests.request("GET", url, headers=header) # 获取网页数据
response.encoding = response.apparent_encoding # 当获取的网页有乱码时加
soup = BeautifulSoup(response.text, 'lxml')
list_con_dd = soup.find('dl')
string = 'https://s3.ananas.chaoxing.com/sv-w9/doc/21/8b/7e/09794316c97672329598184dec5ecf04/thumb/'
for url in range(1, 40):
    stringx = string + str(url) + '.png'
    url_list.append(stringx)
print(url_list)
save_path = 'E:/python/' + str('考试题库')  # 文件夹名
if not os.path.exists(save_path):
    os.mkdir(save_path)
idx = 1
for url in url_list:
    resp = requests.get(url, headers=header)
    print(resp.status_code)
    open(save_path + '/' + str(idx) + '.jpg', 'wb').write(resp.content)  # 将内容写入图片
    idx += 1

import requests
import re

uid = input("_uid=")
client = input("__client_id=")
string = "_uid="+uid+";__client_id="+client # 这里的string为拼接的cookie

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    ,"cookie":string # 使用cookie
}

response = requests.get("https://www.luogu.com.cn",headers=headers)
response.encoding = 'utf-8' # 解码
s = response.text # 获取网页源代码

# 以下程序为正则表达式，在后文会提到，作用为抓取登录洛谷后打卡页面的id
p = re.search(r"<h2 style='margin-bottom: 0'>(.*?)</h2>",s)
if p:
    s=p.group()
    p = re.search(r"target=\"_blank\">(.*?)</a>",s)
    print("成功登录 " + p.group(1))
else:
    p = re.search(r"<h2>欢迎回来，(.*?)</h2>",s)
    if p:
        p = re.search(r"target=\"_blank\">(.*?)</a>",s)
        print("成功登录 " + p.group(1))
    else:
        ref = "https://www.luogu.com.cn/api/user/search?keyword="+uid
        response = requests.get(ref,headers=headers)
        response.encoding = 'utf-8'
        id = response.json()
        id = id['users'][0]["name"]
        print("登录失败","uid:",uid,"id:",id)

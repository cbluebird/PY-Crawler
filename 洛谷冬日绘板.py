import requests
import json
import time

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    ,"cookie":""
}

with open("cookies.json","r") as load_f:
    cookie = json.load(load_f) # 引入cookie
with open("board.json","r") as load_f:
    board = json.load(load_f) # 引入图画内容

def paint(x,y,c): # 涂色函数
    data={
        'x':x,
        'y':y,
        'color':c,
    } # data为我们需要填充的颜色和坐标
    print(x,y,c)
    global cur
    headers["cookie"]=cookie[cur]
    print(data,headers)
    response = requests.post("http://www.luogu.com.cn/paintBoard/paint",data=data,headers=headers) # 填色

pause=31
mark=0
t0 = time.time()
while 1:
    headers["cookie"]=cookie[0]
    pboard = requests.get("http://www.luogu.com.cn/paintBoard/board",headers=headers)
    d=[]
    cnt=1
    for point in board:
        if cnt>len(cookie):
            break
        x=point[0]
        y=point[1]
        c=point[2]
        if int(pboard.text[x*601+y],32) != c:
            cnt=cnt+1
            d.append(point)
    cur=0
    t = time.time()-t0
    # print(t)
    if mark == 1:
        time.sleep(pause-t)
    mark=1
    t0 = time.time()
    for point in d:
        headers["cookie"]=cookie[cur]
        x=point[0]
        y=point[1]
        c=point[2]
        paint(x,y,c)
        cur=cur+1

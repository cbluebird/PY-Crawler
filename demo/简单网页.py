import requests
str ='http://www.baidu.com'
response = requests.get(str)
response.encoding = 'utf-8'
print(response.text)

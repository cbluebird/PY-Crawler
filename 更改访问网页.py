import requests
url=input()
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
response = requests.get(url=url,headers=head)
response.encoding = 'utf-8'
print(response.text)

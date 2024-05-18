import hashlib
import base64
import requests
import json
import time

from urllib.parse import urlencode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(data):
    key = b'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
    iv = b'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
    iv = hashlib.md5(iv).digest()
    key = hashlib.md5(key).digest()

    # AES解密
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = cipher.decrypt(base64.b64decode(data, b'-_'))
    unpadded_message = unpad(decrypted, AES.block_size).decode()
    return unpadded_message


url = 'https://dict.youdao.com/webtranslate'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'referer': 'https://fanyi.youdao.com/',
    'cookie': 'OUTFOX_SEARCH_USER_ID=-805044645@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=818822109.5585971;'
}

t = time.time()

query = {
    'client': 'fanyideskweb',
    'mysticTime': t,
    'product': 'webfanyi',
    'key': 'fsdsogkndfokasodnaso'
}

# 获取sign值 - -密钥值
h = hashlib.md5(urlencode(query).encode('utf-8')).hexdigest()

data = {
    'i': '你好',
    'from': 'zh-CHS',
    'to': 'ja',
    'domain': 0,
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': h,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': t,
    'keyfrom': 'fanyi.web'
}

res = requests.post(url, headers=headers, data=data)
# 翻译结果进行AES解密
ret = json.loads(decrypt(res.text))
tgt = ret['translateResult'][0][0]['tgt']

print('翻译结果：', tgt)





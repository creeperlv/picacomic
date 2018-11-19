import requests

pro = {"https": "https://172.26.14.20:443"}
a = requests.get("https://baidu.com", proxies=pro).text
print(a)
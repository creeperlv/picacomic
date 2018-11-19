from urllib import request, error, parse
import io
import gzip
import http.cookiejar
import re
import os
import threading
import time
from PIL import Image

senddata = {"username": 1715792378, "password": 1715792378, "action": "signin"}
sendhead = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://gentai.org",
    "referer": "https://gentai.org/user",
    "upgrade-insecure-requests": 1,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" +
                  "537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
url = "https://gentai.org/user"
file_root = "E:/gen/"


def login():
    sendd = parse.urlencode(senddata).encode()
    jar = http.cookiejar.MozillaCookieJar("cookies.txt")
    opener = request.build_opener(request.HTTPCookieProcessor(jar))
    header = []
    for i in sendhead:
        tmp = (i, sendhead[i])
        header.append(tmp)
    opener.addheaders = header
    data = opener.open(url, sendd)
    encode = data.getheader("Content-Encoding")
    if encode == 'gzip':
        data = data.read()
        tmp = io.BytesIO(data)
        df = gzip.GzipFile(fileobj=tmp)
    jar.save(ignore_discard=True, ignore_expires=True)
    return opener


def get(num, han):
    try:
        _data = han.open("https://gentai.org/gallery/{0}".format(num)).read().decode()
    except error.HTTPError:
        return
    _data = re.findall("data-src='(.*)'", _data)
    # _data = eval(_data)
    file_tmp = file_root + str(num)
    try:
        os.mkdir(file_tmp)
    except:
        pass
    cnt = 1
    for i in _data:
        da = han.open(i).read()
        print(i)
        Ida = Image.open(io.BytesIO(da))
        Ida.save(file_tmp + "/{0:04}.jpg".format(cnt))
        cnt += 1


if __name__ == "__main__":
    han = login()
    for i in range(5710, 5730):
        t = threading.Thread(target=get, args=(i, han, ))
        while len(threading.enumerate()) > 10:
            time.sleep(10)
        t.start()

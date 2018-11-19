import urllib.request, urllib.response, urllib.parse
import io
import gzip
import http.cookiejar


senddata={"username": 1715792378, "password": 1715792378}
sendhead={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://gentai.org",
    "referer": "https://gentai.org/user",
    "upgrade-insecure-requests": 1,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
url = "https://gentai.org/signin"


def login():
    sendd = urllib.parse.urlencode(senddata).encode()
    jar = http.cookiejar.MozillaCookieJar("cookies.txt")
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
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
    #    data = str(df.read())
    #print(data.read())
    jar.save(ignore_discard=True, ignore_expires=True)
    return opener


if __name__ == "__main__":
    opener = login()
    data = opener.open("https://nl.gentai.org/218/218339/1.webp")
    with open("E:\\1.webp", "wb") as tmp:
        tmp.write(data.read())


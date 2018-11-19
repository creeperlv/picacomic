from urllib import request
import re
import json
import down
url = "https://ecchi.iwara.tv/videos?page={0}"
api = "https://ecchi.iwara.tv/api/video/"
header = {"User-Agent": "Fuck_off", }
proxy_url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"


def test(num):
    req = request.Request(headers=header, url=url.format(num))
    # req.set_proxy("https://153.126.215.31:60088", "https")
    data = request.urlopen(req).read().decode()
    name = re.findall('(?<=<a href="/videos/)[^"?]*', data)
    name = set(name)
    print(name)
    print(len(name))
    for i in name:
        tmpurl = api + i
        req = request.Request(headers=header, url=tmpurl)
        while True:
            data = request.urlopen(req).read().decode()
            data = json.loads(data)
            try:
                realurl = data[0]["uri"]
            except IndexError:
                break
            else:
                try:
                    # fi = down.download(url=realurl,
                    #                    dirpath="E:\\test\\2\\", filename=i + ".mp4", threadnum=32, header=header)
                    print(realurl)

                    break
                except:
                    continue


def test2(num):
    han = request.ProxyHandler({"https": "https://153.126.215.31:60088"})
    opener = request.build_opener(han)
    opener.addheaders = [("User-Agent", "Fuck_off")]
    # req = request.Request(headers=header, url=url.format(num))
    # data = request.urlopen(req).read().decode()
    data = opener.open(url.format(num)).read().decode()
    name = re.findall('(?<=<a href="/videos/)[^"?]*', data)
    name = set(name)
    print(name)
    print(len(name))
    for i in name:
        tmpurl = api + i
        # req = request.Request(headers=header, url=tmpurl)
        while True:
            # data = request.urlopen(req).read().decode()
            data = opener.open(tmpurl).read().decode()
            data = json.loads(data)
            try:
                realurl = "https:" + data[0]["uri"]
            except IndexError:
                break
            else:
                try:
                    # fi = down.download(url=realurl,
                    #                    dirpath="E:\\test\\2\\", filename=i + ".mp4", threadnum=32, header=header)
                    print(realurl)
                    opener.addheaders = [("User-Agent", "Fuck_off")]
                    with open("{}.mp4".format(i), "wb") as _:
                        da = opener.open(realurl)
                        size = da.getheader("Content-Length")
                        print("{0} size:{1}".format(i, size))
                        _.write(da.read(int(size)))
                    return
                except ():
                    print("")


if __name__ == "__main__":
    test2(0)

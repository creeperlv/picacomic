# -*- coding: UTF-8 -*-
import requests
import json
import re
import os
import time
import logging
from urllib import parse
url = 'https://gentai.org/g/src:all/order:date/text:{}?p={}'
logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filemode="w")


def run(word):
    word2 = parse.quote(word)
    div = '<div><img src="{}" id="img_find_me" height="1000"/></div>\n'
    __url = url.format(word2, 3)
    sou = requests.get(__url).text
    a = re.findall("var x = (.*);", sou)[1]
    a = json.loads(a)
    page = a["pages"]
    vis = open("vis.txt").read().split(" ")
    for p in range(1, int(page) + 1):
        __url = url.format(word2, p)
        sou = requests.get(__url).text
        a = re.findall("var x = (.*);", sou)[1]
        a = json.loads(a)
        for i in a["data"]:
            title = i["title"].replace("/", "_")
            if str(i["id"]) in vis:
                continue
            logging.info("start: id:{0} title{1} counts:{2}".format(str(i["id"]), i["title"], len(i["images"])))
            try:
                os.mkdir("gen/#{0}#{1}".format(word.replace("#", ""), title))
            except FileExistsError:
                pass
            with open("./gen/#{0}#{1}/index.html".format(word.replace("#", ""), title), "w") as html_sou:
                ti = time.localtime(i["date"]/10**9)
                html_sou.write('<meta charset="UTF-8">\n')
                html_sou.write("<div>爬取时间：{}</div>\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))
                html_sou.write("<div>上传时间：{}</div>\n".format(time.strftime("%Y-%m-%d %H:%M:%S", ti)))
                html_sou.write("<div>Title：{}</div>\n".format(i["title"]))
                html_sou.write("<div>Tags：{}</div>\n".format(i["tags"]))
                for j in i["images"]:
                    with open("./gen/#{0}#{1}/{2}".format(word.replace("#", ""), title, j.split("/")[-1]), "wb") as tmp:
                        while True:
                            cnt = 0
                            try:
                                img = requests.get("https://img.gentai.org" + j).content
                                break
                            except requests.exceptions.ConnectionError as err:
                                if cnt > 10:
                                    raise Exception("Too many tries")
                                logging.error(err)
                                cnt += 1
                                time.sleep(8)
                        logging.info(j)
                        tmp.write(img)
                        # print(div.format(j.split("/")[-1]))
                        html_sou.write(div.format(j.split("/")[-1]))
                open("vis.txt", "a").write(str(i["id"]) + " ")
                vis.append(str(i["id"]))


if __name__ == "__main__":
    run("#性别变化")

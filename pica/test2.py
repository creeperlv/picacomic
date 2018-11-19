import requests
import re
import time
import sqlite3
import logging
import json
from urllib import parse

logging.basicConfig(filename='gen.log',
                    level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filemode="w")

db = sqlite3.connect("data.db")
cur = db.cursor()


def communicate_db(sql):
    global cur
    try:
        __res = cur.execute(sql).fetchall()
        logging.info(str(__res))
        db.commit()
        return __res
    except sqlite3.OperationalError:
        return []


def search(word):
    word = parse.quote(word)
    __api = "https://gentai.org/?p={1}&q={0}"
    __url = __api.format(word, 1)
    __res = requests.get(__url).text
    # print(len(re.findall("var x = (.*?)};", __res)))
    # __res = re.findall("class\\=title(.*?)\\</a>", __res)
    logging.info(__res)
    pages = int(re.findall("p=(\\d+)", __res)[-1])
    logging.info("pages: {}".format(pages))
    for _ in range(1, pages + 1):
        __url = __api.format(word, _)
        __res = requests.get(__url).text
        __res = re.findall("class\\=title(.*?)\\</a>", __res)
        logging.info(json.dumps(__res))
        for __ in __res:
            idd = re.findall("/gallery/(\\d+)", __)[0]
            name = __.split('"_blank">')[-1]
            if len(communicate_db("select * from crew2 where id='{}';".format(idd))) > 0:
                continue
            # data = json.dumps(__["images"])
            while True:
                _res = requests.get("https://gentai.org/gallery/{}?view=1".format(idd))
                if _res.status_code != 200:
                    time.sleep(10)
                    continue
                break
            data = re.findall("/img/([0-9/]{10})", _res.text)[0]
            page = re.findall("共(\\d+)", _res.text)[0]
            communicate_db("insert into crew2(id,name,data,pages)values('{}','{}','{}',{});".format(idd, name, data, page))

if __name__ == "__main__":
    communicate_db("create table crew2(id text PRIMARY KEY,name text,data text,pages integer);")
    search("#")

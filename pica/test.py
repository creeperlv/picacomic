# -*- coding: utf-8 -*-
import re
import hmac
import time
import json
import uuid
import zipfile
import urllib3
import sqlite3
import logging
import hashlib
import platform
import requests
from urllib import parse
logging.basicConfig(filename='pica.log',
                    level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filemode="w")
urllib3.disable_warnings()
global_url = "https://picaapi.picacomic.com/"
api_key = "C69BAF41DA5ABD1FFEDC6D2FEA56B"
secret_key = "~n}$S9$lGts=U)8zfL/R.PM9;4[3|@/CEsl~Kk!7?BYZ:BAa5zkkRBL7r|1/*Cr"
uuid_s = str(uuid.uuid4()).replace("-", "")
header = {
        "api-key": "C69BAF41DA5ABD1FFEDC6D2FEA56B",
        "accept": "application/vnd.picacomic.com.v1+json",
        "app-channel": "2",
        "time": 0,
        "nonce": "",
        "signature": "encrypt",
        "app-version": "2.1.0.4",
        "app-uuid": "418e56fb-60fb-352b-8fca-c6e8f0737ce6",
        "app-platform": "android",
        "app-build-version": "39",
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "okhttp/3.8.1",
}


class Pica:

    def __init__(self, account, password):
        self.path = "D:/pic/" if platform.system() == 'Windows' else "/mnt/usb/gen/"
        self.account = account
        self.password = password
        self.header = header.copy()
        self.uuid_s = str(uuid.uuid4()).replace("-", "")
        self.header["nonce"] = self.uuid_s
        self.db = sqlite3.connect("data.db")
        self.communicate_db("create table account (email text PRIMARY KEY NOT NULL, password text, key text);")
        # self.communicate_db("create table crew (id text PRIMARY KEY NOT NULL, title text, );")
        self.communicate_db("create table crew (id text PRIMARY KEY NOT NULL,name text,data text);")
        self.check()

    def communicate_db(self, sql):
        cur = self.db.cursor()
        try:
            __res = cur.execute(sql).fetchall()
            logging.info(str(__res))
            self.db.commit()
            return __res
        except sqlite3.OperationalError:
            return []

    def check(self):
        token = self.communicate_db("select key from account where email='{}';".format(self.account))
        if len(token) == 0:
            token = self.login()
            self.communicate_db("insert into account (email, password, key)" +
                                "values ('{0}', '{1}', '{2}');".format(self.account, self.password, token))
            return
        token = token[0][0]
        self.header["authorization"] = token
        __res = self.get(global_url + "users/profile")
        try:
            __res = __res.json()
        except json.JSONDecodeError:
            logging.error(__res.text)
            raise json.JSONDecodeError
        # print(__res)
        # print(token)
        if __res["code"] != 200:
            token = self.login()
            self.communicate_db("update test set key='{0}' where email='{1}';".format(token, self.account))

    def post(self, url, data=None):
        ts = str(int(time.time()))
        self.header["time"] = ts
        self.header["signature"] = self.encrypt(url, ts, "POST", self.uuid_s)
        return requests.post(url=url, data=data, headers=self.header, verify=False)

    def get(self, url):
        ts = str(int(time.time()))
        self.header["time"] = ts
        self.header["signature"] = self.encrypt(url, ts, "GET", self.uuid_s)
        header_tmp = self.header.copy()
        header_tmp.pop("Content-Type")
        return requests.get(url=url, headers=header_tmp, verify=False)

    @staticmethod
    def encrypt(url, ts, method, uuid_ss):
        """

        :param url: 完整链接：https://picaapi.picacomic.com/auth/sign-in
        :param ts: 要和head里面的time一致, int(time.time())
        :param method: http请求方式: "GET" or "POST"
        :param uuid_ss: str, len(uuid)==32
        :return: header["signature"]
        """
        raw = url.replace("https://picaapi.picacomic.com/", "") + str(ts) + uuid_ss + method + api_key
        raw = raw.lower()
        hc = hmac.new(secret_key.encode(), digestmod=hashlib.sha256)
        hc.update(raw.encode())
        return hc.hexdigest()

    def login(self):
        api = "auth/sign-in"
        url = global_url + api
        send = {"email": self.account, "password": self.password}
        __a = self.post(url=url, data=json.dumps(send)).text
        logging.info(__a)
        self.header["authorization"] = json.loads(__a)["data"]["token"]
        return self.header["authorization"]

    def categories(self):
        api = "categories"
        url = global_url + api
        return self.get(url)

    def block(self, __page, bl):
        api = "comics?page={0}&c={1}&s=ua".format(__page, bl)
        url = global_url + api
        return self.get(url)

    def comics(self, __id, __name):
        api = global_url + "comics/{0}/eps?".format(__id) + "page={0}"
        url = api.format(1)
        _return = []
        __pages = self.get(url).json()["data"]["eps"]["pages"]
        for _ in range(1, __pages + 1):  # __pages + 1
            url = api.format(_)
            __res = self.get(url).json()["data"]["eps"]["docs"]
            for __ in __res:
                if len(self.communicate_db("select * from crew where id='{}';".format(__["_id"]))) > 0:
                    continue
                _name = re.sub("[|:/*]*", "", __name + __["title"])
                logging.info(_name)
                _return.append({"name": _name, "fid": __id, "order": __["order"], "id": __["_id"]})
        return _return

    def comic(self, __order, __id):
        api = global_url + 'comics/{0}/order/{1}/pages'.format(__id, __order) + '?page={0}'
        url = api.format(1)
        _return = []
        __pages = self.get(url).json()["data"]["pages"]["pages"]
        for _ in range(1, __pages + 1):  # __pages + 1
            url = api.format(_)
            __res = self.get(url).json()["data"]["pages"]["docs"]
            for __ in __res:
                _tmp = __["media"]
                _return.append(_tmp["path"])  # "name": _tmp["originalName"], "url": _tmp["path"]
        # _tmp["fileServer"] + "/static/" +  https://storage1.picacomic.com/static/
        return _return

    def get_picture(self, url):
        while True:
            try:
                __a = self.get(url)
                break
            except requests.exceptions.ConnectionError:
                logging.error("get picture failed: " + url)
                time.sleep(8)
        return __a.content

    def search(self, __word):
        api = global_url + "comics/search?page={0}" + "&q={0}".format(parse.quote(__word))
        url = api.format(1)
        __pages = self.get(url).json()["data"]["comics"]["pages"]
        _return = []
        for _ in range(1, 2):  # __pages + 1
            url = api.format(_)
            __res = self.get(url).json()["data"]["comics"]["docs"]
            for __ in __res:
                _return.append({"name": __["title"], "id": __["_id"]})
        return _return


if __name__ == "__main__":
    insert = """
        insert into crew(id,name,data)values('{0}','{1}','{2}');
    """
    s = Pica("robottest@163.com", "robottest")
    div = '<div><img src="{}"/></div>\n'
    want = "少女映画"
    res = s.search(want)
    comic = []
    # out_zip = zipfile.ZipFile(s.path + "out.zip", "x", compression=zipfile.ZIP_DEFLATED)
    for i in res:
        logging.info(json.dumps(i))
        comic += s.comics(i["id"], i["name"])
    for i in comic:
        # if int(time.strftime("%H%M")) > 2300:
        #     break
        pic = s.comic(i["order"], i["fid"])
        logging.info("start: {0} counts: {1}".format(i["name"], len(pic)))
        data = json.dumps(pic)
        # print(data)
        s.communicate_db(insert.format(i["id"], i["name"], data))
        # work = s.path
        # for j in pic:
            # logging.info("\t" + j["url"])
            # print("https://storage1.picacomic.com/static/" + j["url"])

            # pic_b = s.get_picture(j["url"])
            # open(work + "tmp", "wb").write(pic_b)
            # with zipfile.ZipFile(s.path + "out.zip", "a", compression=zipfile.ZIP_DEFLATED) as out_zip:
            #     with out_zip.open("{}/{}".format(i["name"], j["name"]), "w") as out:
            #         out.write(pic_b)
        # s.communicate_db("insert into crew (id) values ('{}')".format(i["id"]))
        # break

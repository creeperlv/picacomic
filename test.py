import hmac
import hashlib

uuid = "28001bae24614ee5bae1c2ca5328aabc"
api_key = "C69BAF41DA5ABD1FFEDC6D2FEA56B"
secret_key = "~n}$S9$lGts=U)8zfL/R.PM9;4[3|@/CEsl~Kk!7?BYZ:BAa5zkkRBL7r|1/*Cr"
version = "2.1.0.4"
build_version = "39"
channel = 2
header = {
        "api-key": "C69BAF41DA5ABD1FFEDC6D2FEA56B",
        "accept": "application/vnd.picacomic.com.v1+json",
        "app-channel": channel,
        "time": 0,
        "nonce": uuid,
        "signature": "encrypt",
        "app-version": version,
        "app-uuid": "1b509109-476d-3790-a5f0-0acfeace9a5b",
        "app-platform": "android",
        "app-build-version": build_version
}


def encrypt(url, ts, method):
    """

    :param url: 完整链接：https://picaapi.picacomic.com/auth/sign-in
    :param ts: 要和head里面的time一致, int(time.time())
    :param method: http请求方式: "GET" or "POST"
    :return: header["signature"]
    """
    raw = url.replace("https://picaapi.picacomic.com/", "") + str(ts) + uuid + method + api_key
    raw = raw.lower()
    hc = hmac.new(secret_key.encode(), digestmod=hashlib.sha256)
    hc.update(raw.encode())
    return hc.hexdigest()


if __name__ == "__main__":
    encrypt("https://picaapi.picacomic.com/announcements?page=1", 1533301254, 'GET')

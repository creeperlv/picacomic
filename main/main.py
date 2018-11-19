import socket
import requests
import json
import gzip

a = gzip.open("D:/t.gzip", "wb")
o = open("D:/1.pdf", "rb").read()
a.write(o)
a.close()

import gzip
import io


def dezip(source, *, codeform="utf-8"):
    if source.getheader("Content-Encoding") == "gzip":
        tmp = io.BytesIO(source.read())
        data = gzip.GzipFile(fileobj=tmp).read().decode(codeform)
    else:
        data = source.read().decode(codeform)
    return data

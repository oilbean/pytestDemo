import base64


def encode_base64(a):
    a = a.encode("utf-8")

    return base64.b64encode(a)

def decode_base64(a):
    return base64.b64decode(a)
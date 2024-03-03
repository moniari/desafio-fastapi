from base64 import b64decode
from uu import encode


def decodeBase64(encodedToken: str):
    ascii_encode = encodedToken.encode("ascii")
    base64_decoded = b64decode(ascii_encode)
    ascii_decoded = base64_decoded.decode("ascii")

    return ascii_decoded.split(':')
    

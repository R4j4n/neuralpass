# Get key using user provided 4 digit pin
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def getKey(key):
    keyEncoded = key.encode()
    salt = b'\xba\x80\xb4\xb2|&\xd6"$\x0f\x01\x89ZC:P'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                     salt=salt, iterations=1000000, backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(keyEncoded))

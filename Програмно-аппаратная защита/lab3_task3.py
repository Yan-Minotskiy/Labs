import secrets
import hashlib


p=secrets.token_bytes(32)
while True:
    h=hashlib.sha256(p).digest()
    if h.hex()[:4] == '0' * 4: 
        break
    p=h
print('SHA256(' + p.hex() + ')=' + h.hex())

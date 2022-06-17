import sys
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

filename = sys.argv[1]
public_key_path = sys.argv[2]

# получение ключей
with open(public_key_path, "rb") as f:
    key = RSA.import_key(f.read())
session_key = get_random_bytes(16)

# шифрование
with open(filename, "rb") as f:
    content = f.read()
with open(filename, "wb") as f:
    cipher_rsa = PKCS1_OAEP.new(key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(content)
    [f.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

filename = sys.argv[1]
private_key_path = sys.argv[2]

# получение приватного ключа
with open(private_key_path, "rb") as f:
    key = RSA.import_key(f.read())

# расшифровка
with open(filename, "rb") as f:
    enc_session_key, nonce, tag, ciphertext = [f.read(x) for x in (key.size_in_bytes(), 16, 16, -1)]
cipher_rsa = PKCS1_OAEP.new(key)
session_key = cipher_rsa.decrypt(enc_session_key)
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
content = cipher_aes.decrypt_and_verify(ciphertext, tag)
with open(filename, "wb") as f:
    f.write(content)

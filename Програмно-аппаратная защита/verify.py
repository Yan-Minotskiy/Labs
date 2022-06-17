import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

filename = sys.args[1]
public_key_path = sys.argv[2]

# получаем публичный ключ
with open(public_key_path, "rb") as f:
    key = RSA.import_key(f.read())

# извлечение подписи из файла
with open(filename, "rb") as f:
    content = f.read()
    with open("temp.temp", 'wb') as temp_file:
        temp_file.write(content[:-128])
    signature = content[-128:]

# получаем хэш файла
h = SHA256.new()
with open("temp.temp", "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)

# проверка подписи
pkcs1_15.new(key).verify(h, signature)

# удаляем временный файл
os.remove("temp.temp")

print("SUCCESSFULLY VERIFIED")

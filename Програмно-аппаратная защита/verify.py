import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

filename = sys.args[1]
public_key_path = sys.argv[2]

# �������� ��������� ����
with open(public_key_path, "rb") as f:
    key = RSA.import_key(f.read())

# ���������� ������� �� �����
with open(filename, "rb") as f:
    content = f.read()
    with open("temp.temp", 'wb') as temp_file:
        temp_file.write(content[:-128])
    signature = content[-128:]

# �������� ��� �����
h = SHA256.new()
with open("temp.temp", "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)

# �������� �������
pkcs1_15.new(key).verify(h, signature)

# ������� ��������� ����
os.remove("temp.temp")

print("SUCCESSFULLY VERIFIED")

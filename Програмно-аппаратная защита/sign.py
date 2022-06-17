import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

filename = sys.args[1]
private_key_path = sys.argv[2]

# �������� ��������� ���� 
with open(private_key_path, "rb") as f:
    key = RSA.import_key(f.read())

# �������� ��� �����
h = SHA256.new()
with open(filename, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)

# ����������� ����
signature = pkcs1_15.new(key).sign(h)
with open(filename, 'rb') as f:
    content = f.read()
with open(filename, 'wb') as f:
    f.write(content + signature)
print("SUCCESSFULLY SIGNED")
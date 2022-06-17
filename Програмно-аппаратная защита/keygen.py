import os
from Crypto.PublicKey import RSA

private_key = RSA.generate(1024, os.urandom)
public_key = private_key.publickey()
with open("private_key.pem", 'wb') as f:
    f.write(private_key.exportKey("PEM"))
with open("public_key.pem", 'wb') as f:
    f.write(public_key.exportKey("PEM"))
print("SUCCESSFULLY CREATED")
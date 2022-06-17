import rsa

# генерация ключей
(pubkey, privkey) = rsa.newkeys(2048)
 
# шифрование 
message = 'ЯН'
crypto = rsa.encrypt(message.encode('utf-8'), pubkey)

#расшифровка и вывод
message = rsa.decrypt(crypto, privkey)
print(message.decode('utf-8'))

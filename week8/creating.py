from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('mykey.key','rb') as mykey:
    key = mykey.read()
print(key)
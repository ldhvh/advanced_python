from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('mykey.key','rb') as mykey:
    key = mykey.read()
f = Fernet(key)

with open('enc_grades.csv','rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_grades.csv','wb') as decrypted_file:
    decrypted_file.write(decrypted)
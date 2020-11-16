!pip install cryptography
from cryptography.fernet import Fernet

## 1 Solution


file1 = open("Please put here file Path","r+").read()
file1 = str.encode(file1)
print(file1)

Secret_key = open("Please Put here SecretKey Path", "rb").read()
print(Secret_key)

decrypt_manual = Fernet(Secret_key).decrypt(file1)
print(decrypt_manual.decode())

## 2 Solution

#The funtion desencriptar need the arguments Secret key and the file
def desencriptar(key, file):
    Secret_key = open(key, "rb").read()
    file1 = open(file,"r+").read()
    #if we have more data type we can put more if statements
    if type(file1) == str:
      file1 = str.encode(file1)
    decrypt_manual = Fernet(Secret_key).decrypt(file1)
    print(decrypt_manual.decode())

desencriptar("lease put here file Path","Please Put here SecretKey Path")

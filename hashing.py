import hashlib
import cgi, cgitb
import os

def HashearString(cadena):
    StringEnBytes=cadena.encode()
    print(type(StringEnBytes))
    hashString= hashlib.sha256(StringEnBytes)
    return hashString.digest()

def HashearBytes(archbytes):
    hashbytes= hashlib.sha256(archbytes)
    return hashbytes.digest()



def SaltGenerator(size):
    Salt=str(os.urandom(size))
    return Salt

def CompararHashes(hash1,hash2):
    if len(hash1) !=len(hash2):
        return False
    else:
         for i in range ( len(hash1)):
            if hash1[i]!=hash2[i]:
                return False
         return True    

print(HashearString("hola"))

import hashlib
import cgi, cgitb
import os

def HashearString(cadena):
    StringEnBytes=cadena.encode()
    hashString= hashlib.sha256(StringEnBytes)
    return hashString.digest()


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

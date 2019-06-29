#PROYECTO DE SEGURIDAD INFORMATICA

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import hashlib
from os import listdir
from os.path import isfile, join

class Encryptor:
    def __init__(self,key):
        self.key = key

    def pad(self,s):
        return s+b"\0" *(AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size = 256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def enc_full_File(self, file_name):
        f = open(file_name, 'rb')
        enc = self.encrypt(f, self.key)
        with open(file_name + ".encf", "wb") as f:
            f.write(enc)
        os.remove(file_name)

def encriptarArchivo(usuario,pathfrase,ruta):
    try:
        result=False
        #Guardar pathfrase en el hash
        key = hashlib.sha256(pathfrase.encode('utf-8')).digest()
        print(key)
        #key = str(key).replace(',', '.')
        #print(key)
        encriptador = Encryptor(key)
        encriptador.encrypt_file(ruta)
        rutaUsuarios = "/Users/Usuario/Documents/Flask/ArchivosParaEncriptar/usuarioarchivo.txt"
        with open(rutaUsuarios, 'a') as file:
            linea = str(usuario) + "," + str(key) + "," + str(ruta + ".enc")
            file.write(linea)
            result= True
        return result
  
    except :
        return False

def desencriptarArchivo(usuario, pathfrase, ruta):
    #Checkear si la key es la que se encuentra hasheada
    result = False
    key = hashlib.sha256(pathfrase.encode('utf-8')).digest()
    rutaUsuarios = "/Users/Usuario/Documents/Flask/ArchivosParaEncriptar/usuarioarchivo.txt"
    with open(rutaUsuarios, 'r') as file:
        lines = file.readlines()
    with open(rutaUsuarios, 'r') as file:
        for usuarioArchivo in lines:
            usuarioArchivoArr = usuarioArchivo.split(",")
            print(usuarioArchivoArr)
            if usuarioArchivoArr[0] == usuario:
                print("1")
                if usuarioArchivoArr[1] == str(key):
                    print("1")
                    if usuarioArchivoArr[2] == ruta:
                        print("1")
                        encriptador = Encryptor(key)
                        encriptador.decrypt_file(ruta)
                        result = True
    return result
                
        
        
                                

    
        
        



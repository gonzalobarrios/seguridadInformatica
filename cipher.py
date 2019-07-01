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
        key = hashlib.sha256(pathfrase.encode('utf-8')).digest()
        encriptador = Encryptor(key)
        encriptador.encrypt_file(ruta)
      
        rutaUsuarios = "/Users/Usuario/Documents/Flask/ArchivosParaEncriptar/usuarioarchivo.txt"
        with open(rutaUsuarios, 'a') as file:
            linea = str(usuario) + "," + str(key) + "," + str(ruta + ".enc")
            file.write(linea)
            file.write("\n")
        file.close()
    except:
        return False
    return True

def desencriptarArchivo(usuario, pathfrase, ruta):
    res = False
    key = hashlib.sha256(pathfrase.encode('utf-8')).digest()
    rutaUsuarios = "/Users/Usuario/Documents/Flask/ArchivosParaEncriptar/usuarioarchivo.txt"
    try:
        with open(rutaUsuarios, 'r') as file:
            lines = file.readlines()
        file.close()
        with open(rutaUsuarios, 'w') as fileOut:
            for usuarioArchivo in lines:
                if len(usuarioArchivo.split(",")) >=3:
                    usuarioArchivoArr = obtenerDatos(usuarioArchivo)
                    if (usuarioArchivoArr[0] == usuario) and (usuarioArchivoArr[1] == str(key)) and (usuarioArchivoArr[2].rstrip("\n") == ruta):
                        encriptador = Encryptor(key)
                        encriptador.decrypt_file(ruta)
                        res = True
                    else:
                        fileOut.write(usuarioArchivo)
        fileOut.close()
    except:
        return False
    return res

def obtenerDatos(linea):
    datos = linea.split(",")
    usuario = datos[0]
    key = ""
    ruta = datos[len(datos) -1]
    if len(datos) > 3:
        datosKey = (datos[1:len(datos)-1])
        key = datosKey[0]
        for i in range(1,len(datosKey)):
            key += "," + datosKey[i]
    elif len(datos) <= 3:
        key = datos[1]
    return [usuario,key,ruta]



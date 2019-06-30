import Crypto
import hashing
import loguear
import registros
import cipher
import rsa

def firmararchivo(usuario,file_name):
    keypublica,keyprivada = rsa.newkeys(2048)

    #Obtiene el documento a firmar
    with open(file_name, 'rb') as fo:
        documento = fo.read()

    #Obtiene la firma del documento
    firma = rsa.sign(documento, keyprivada, hashAlg="SHA-256")

    #Guarda la firma del documento
    with open(file_name + ".firma", 'wb') as fo:
        fo.write(firma)

    keypublica.exportKey(format='PEM')
    #Guarda la clave publica
    with open("public.pem", "wb") as pub_file:
        pub_file.write(keypublica.exportKey('PEM'))

    return True

def validararchivo(usuario,file_name):

    #Obtiene el documento firmado
    with open(file_name, 'rb') as fo:
        documento = fo.read()

    #Obtiene la firma del documento
    with open(file_name + ".firma", 'rb') as fo:
        firma = fo.read()

    #Obtiene la clave publica
    with open("public.pem", "rb") as pub_file:
        keypublica = rsa.importKey(pub_file.read())

    #Valida el documento y la firma con la clave publica
    validacion = rsa.verify(documento, firma, keypublica)

    return validacion
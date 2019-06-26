import hashlib
import cgi, cgitb
import os
import hashing

class Usuario :
    def __init__(self,user,contra,salto):
        self.usuario=user
        self.contra=contra
        self.salto=salto

    def __str__(self):
        return "Usuario {0} y pass {1} y salto {2}".format(self.usuario,self.contra,self.salto)




def BuscarUsuario(usuario,ruta):
    archivo=open(ruta)
    UserObject=None
    for linea in archivo:
        linea=linea.strip().split('@')
        if(len(linea)%3==0):    
            if(linea[0]==usuario):
                user=linea[0]
                contra=linea[1]
                salto=linea[2]
                UserObject=Usuario(user,contra,salto)
    archivo.close()
    return UserObject



def RegistrarUsuario(usuario,password,ruta):

    UserObject = None
    UsuarioRegistrado = BuscarUsuario(usuario, ruta)

    if UsuarioRegistrado is not None:
        print("usuario ya registrado previamente")
    else:

        #print("vamos a registrar usuario nuevo")

        NewSalt=SaltGenerator(32)
        Hash=HashearString(password + NewSalt )
        NewUser=usuario + "@" + str(Hash) + "@" + NewSalt
        archivo = open(ruta, "a")
        archivo.write(NewUser.strip())
        archivo.write("\n")
        archivo.close()
    return UserObject


def Loguear(user,contra):
    UsuarioRegistrado=BuscarUsuario(user,"usuarios.txt")
    Comparacion=False
    if UsuarioRegistrado is not None:
        SaltoUsuarioRegistrado=UsuarioRegistrado.salto
        ContraUsuarioYSalto =contra+SaltoUsuarioRegistrado
        HashDeUsuarioActual=hashing.HashearString(ContraUsuarioYSalto)
        HashUsuarioRegistrado= UsuarioRegistrado.contra
        Comparacion=hashing.CompararHashes(str(HashDeUsuarioActual),HashUsuarioRegistrado)
    return Comparacion
    



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
         print(""""
        <body>
        <div align="left">
     
        <label>"""+"Usuario previamente registrado""""</label>

        <div class="opciones">
                                <button type="button" class="save" onclick="window.location.href='javascript:history.back()'">Volver</button>
                        </div>
        <form >
        """)
    else:

        #print("vamos a registrar usuario nuevo")

        NewSalt=SaltGenerator(32)
        Hash=HashearString(password + NewSalt )
        NewUser=usuario + "@" + str(Hash) + "@" + NewSalt
        archivo = open(ruta, "a")
        archivo.write(NewUser.strip())
        archivo.write("\n")
        archivo.close()
        
        print("""<html><head>
    
        </head>
        <body>
        <div align="left">
        <form >
        <label>"""+"Registro exitoso""""</label>

        <div class="opciones">
                                <button type="button" class="save" onclick="window.location.href='javascript:history.back()'">Volver</button>
                         </div>
         """)
    
    return UserObject

# """""""'"  MAIN """"

params = cgi.FieldStorage()
print ("Content-Type: text/html")
print ("")
print ("")


try:
   
    user=str(params.getvalue("Usuario"))
    contra=str(params.getvalue("Contrasena1"))
    print(user)
    print(contra)
    from hashing import *
    test=RegistrarUsuario(user, contra, "cgi-bin\\usuarios.txt")

    

except:
    print("no se pudo completar la tarea")

        
  



import hashlib
import cgi, cgitb
class Usuario :
    def __init__(self,user,contra,salto):
        self.usuario=user
        self.contra=contra
        self.salto=salto

    def __str__(self):
        return "Usuario {0} y pass {1} y salto {2}".format(self.usuario,self.contra,self.salto)


def HashearString(string):
    StringEnBytes=string.encode()
    hash= hashlib.sha256(StringEnBytes)
    return hash.digest()


def BuscarUsuario(usuario,ruta):
    archivo=open(ruta)
    for linea in archivo:
        linea=linea.strip().split(',')
        if(len(linea)%3==0):    
            if(linea[0]==usuario):
                user=linea[0]
                contra=linea[1]
                salto=linea[2]
                UserObject=Usuario(user,contra,salto)
    archivo.close()
    return UserObject

def CompararHashes(hash1,hash2):
    if len(hash1) !=len(hash2):
       return False
    else:
         for i in range ( len(hash1)):
            if hash1[i]!=hash2[i]:
                return False
         return True    
   


def logIn(usuario,contra):
    #ValidarDatos(usuario,contra)"
    return 0



#tomar parametros y hashear
#buscar en el archivo 
#comparar hashes
#mostrar mensaje
#ver lo del salto, cambia comparacion

# """""""'"  MAIN """"

params = cgi.FieldStorage()
print ("Content-Type: text/html")
print ("")
print ("Content-Type: text/html")
print ("")
print ("<html>")
print ("<body>")
print ("Hola Muchachos!")
print ("</body>")
print ("</html>")

try:
   
    user=params.getvalue("Usuario")
    contra=params.getvalue("Contraseña")
    UsuarioRegistrado=BuscarUsuario(user, "C:\\Users\\Usuario\\Desktop\\Nueva carpeta\\Usuarios.txt")
    Comparacion=False
    if UsuarioRegistrado !=None:
        SaltoUsuarioRegistrado=UsuarioRegistrado.salto
        HashDeUsuarioActual=HashearString(contra++SaltoUsuarioRegistrado)
        HashUsuarioRegistrado= UsuarioRegistrado.contra

        Comparacion=CompararHashes(HashDeUsuarioActual,HashUsuarioRegistrado)

    if(Comparacion):
        print("Logueo exitoso")
    else:
            print("Usuario y/o contraseñas incorrectos")

except:
    print("no se pudo completar la tarea")

#print(m.digest())



"""--------------------"""
"""PRUEBAS"""

user="Manolito" 
root="C:\\Users\\Usuario\\Desktop\\Nueva carpeta\\Usuarios.txt"
ObjetoBuscado= BuscarUsuario( user,root)
print(ObjetoBuscado.contra)

m = hashlib.sha256(b"hola")
a=CompararHashes(HashearString("hola1"),m.digest())








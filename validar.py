#import rsa
import hashing
#def validar(rutaArchivo, rutaFirma):




def encrypt(self, message, key, key_size = 256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
    
def hashFile( file_name):
    with open(file_name, 'rb') as fo:
            plaintext = fo.read()
    archivoHasheado = hashing.HashearBytes(plaintext)
    return archivoHasheado


hashFile("hashing.txt")

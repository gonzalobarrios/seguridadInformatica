from flask import Flask, render_template,redirect, url_for, request
import hashing
import loguear
import registros
import cipher
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Layout.html')

@app.route('/inicio')
def inicio():
  return render_template('login.html')  

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user=request.form['username']
        contra= request.form['password'] 
        Comparacion=loguear.Loguear(user,contra)
        if Comparacion:
                error = 'logueo exitoso'
                sesion=user
                return render_template('formEncriptar.html')  
               
        else:
              error = 'Invalid Credentials. Please try again.'
             
    return render_template('login.html', error=error)


sesion=""
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        user=request.form['username']
        contra= request.form['password']
  
        test=registros.Registrar(user, contra)
        if test is None:
                error = 'usuario ya registrado'
               
        else:
              error = 'usuario registrado exitosamente'
             
    return render_template('login.html', error=error)

@app.route('/encriptar', methods=['GET', 'POST'])
def encriptar():
    error = None
    if request.method == 'POST':
        ruta= request.form['Ruta']
        passprhase= request.form['Passphrase']
        operacion=cipher.Encryptar(sesion, ruta, passprhase)
        if operacion==False:
                error = 'ruta no encontrado'
               
        else:
              error = 'archivo cifrado exitosamente'
             
    return render_template('formEncriptar.html', error=error)


    
@app.route('/descifrar', methods=['GET', 'POST'])
def descifrar():
    error = None
    if request.method == 'POST':
        ruta= request.form['Ruta']
        passprhase= request.form['Passphrase']
        operacion=cipher.Encrypt_file(user,ruta, passprhase)
        if operacion==False:
                error = "clave incorrecta o ruta no encontrada"
               
               
        else:
              error = 'usuario descrifrado exitosamente'
             
    return render_template('formEncriptar.html', error=error)


    
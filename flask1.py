from flask import Flask, render_template,flash,redirect, url_for, request
import hashing
import loguear
import registros
import cipher
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def home():
    return render_template('Layout.html')

@app.route('/inicio')
def inicio():
  return render_template('login.html')  

@app.route('/encriptacionArchivos')
def encriptacionArchivos():
  return render_template('FormEncriptar.html')  



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user=request.form['username']
        contra= request.form['password'] 
        Comparacion=loguear.Loguear(user,contra)

        if Comparacion:
              
              
                flash(f'Logueo exitoso', 'success')
                sesion=user
                return  redirect(url_for('encriptacionArchivos'))
                
        else:
              flash(f'Datos inválidos. Intente de nuevo', 'danger')
        return render_template('login.html')


sesion=""
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        user=request.form['username']
        contra= request.form['password']
        confirm= request.form['Confirm password']
        if confirm==contra:
                test=registros.Registrar(user, contra)
                if test is None:
                        flash(f'Usuario en uso. El usuario debe ser único', 'danger')
                
                else:    
                        flash(f'Usuario registrado exitosamente', 'success')
                       
        else:
               
                flash(f'Las contraseñas no coinciden', 'danger')
                
        return render_template('login.html', error=error)

@app.route('/encriptar', methods=['GET', 'POST'])
def encriptar():
    error = None
    if request.method == 'POST':
        ruta= request.form['Ruta']
        passprhase= request.form['Passphrase']
        confirm= request.form['Confirm Passphrase']
        if confirm==passprhase:
                operacion=cipher.encriptarArchivo(sesion, passprhase, ruta.strip())
                if operacion==False:
                
                        flash(f'Ruta no encontrada', 'danger')
                
                else:
                         flash(f'Archivo cifrado exitosamente', 'success')
        else:
                 flash(f'Las passphrase no coinciden. Intente de nuevo', 'danger')
                
             
    return render_template('formEncriptar.html', error=error)


    
@app.route('/descifrar', methods=['GET', 'POST'])
def descifrar():
    error = None
    if request.method == 'POST':
        ruta= request.form['Ruta']
        passprhase= request.form['Passphrase']
        operacion=cipher.desencriptarArchivo(sesion, passprhase, ruta.strip())
        if operacion==False:
                flash(f'Ruta no encontrada o passphrase incorrecta', 'danger')
              
               
               
        else:
              flash(f'Archivo descrifrado exitosamente', 'success')
             
    return render_template('formEncriptar.html', error=error)


    
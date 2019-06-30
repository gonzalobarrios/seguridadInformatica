from flask import Flask, render_template, flash, redirect, url_for, request
import hashing
import loguear
import registros
import cipher
import rsa
import firma

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


@app.route('/formOpciones')
def formOpciones():
    return render_template('formOpciones.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        contra = request.form['password']
        Comparacion = loguear.Loguear(user, contra)

        if Comparacion:

            flash(f'Logueo exitoso', 'success')
            sesion = user
            return redirect(url_for('formOpciones'))

        else:
            flash(f'Datos inválidos. Intente de nuevo', 'danger')
        return render_template('login.html')


sesion = ""


@app.route('/cifrar')
def cifrar():
    return render_template('formEncriptar.html')

@app.route('/firmar')
def firmar():
    return render_template('formFirmar.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':

        user = request.form['username']
        contra = request.form['password']
        confirm = request.form['Confirm password']
        if confirm == contra:
            test = registros.Registrar(user, contra)
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

        ruta = request.form['Ruta']
        passprhase = request.form['Passphrase']
        confirm = request.form['Confirm Passphrase']
        if confirm == passprhase:
            operacion = cipher.encriptarArchivo(sesion, passprhase, ruta.strip())
            if operacion == False:

                flash(f'Ruta no encontrada', 'danger')

            else:
                flash(f'Archivo cifrado exitosamente', 'success')
        else:
            flash(f'Las passphrase no coinciden. Intente de nuevo', 'danger')

        ruta = request.form['Ruta']

        passprhase = request.form['Passphrase']
        confirmpassprhase = request.form['Confirm Passphrase']

        if passprhase == confirmpassprhase:

            operacion = cipher.encriptarArchivo(sesion, passprhase, ruta.strip())
            if operacion == False:
                error = 'ruta no encontrada o datos incorrectos'

            else:
                error = 'archivo cifrado exitosamente'
        else:
            error = 'La confirmación de passphrase es incorrecta'
    return render_template('formEncriptar.html', error=error)


@app.route('/descifrar', methods=['GET', 'POST'])
def descifrar():
    error = None
    if request.method == 'POST':
        ruta = request.form['Ruta']
        passprhase = request.form['Passphrase']
        operacion = cipher.desencriptarArchivo(sesion, passprhase, ruta.strip())
        if operacion == False:
            flash(f'Ruta no encontrada o passphrase incorrecta', 'danger')

        else:
            flash(f'Archivo descrifrado exitosamente', 'success')

    return render_template('formEncriptar.html', error=error)


@app.route('/firmadigital', methods=['GET', 'POST'])
def firmadigital():
    error = None
    if request.method == 'POST':
        ruta = request.form['Ruta']

        validacion = firma.firmararchivo(sesion,ruta.strip())
        if validacion:
            error = 'Archivo firmado exitosamente'

        else:
            error = 'No se pudo firmar el archivo'

    return render_template('formFirmar.html', error=error)

@app.route('/verificarfirma', methods=['GET', 'POST'])
def verificarfirma():
    error = None
    if request.method == 'POST':
        ruta = request.form['Ruta']

        validacion = firma.validararchivo(sesion, ruta.strip())
        if validacion:
            error = 'Firma verificada exitosamente'

        else:
            error = 'No se pudo verificar la firma del archivo'

    return render_template('formFirmar.html', error=error)
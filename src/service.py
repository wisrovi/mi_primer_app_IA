from flask import Flask, jsonify, request, redirect, make_response
#from werkzeug import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)


nombreParametrosRecibirPost = {
    "Imagen": 'file1',
    "Imagen2": 'file2',
    "NombreImagen": "nameFile",
    "Documento": "document"
}

htmlRta = {
    "index":
        '''
    <!doctype html>
    <title>Servidor IA</title>
    <h1>Servidor de Reconocimiento gatos y perros WISROVI</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=%s>
         <input type=submit value=Upload>
    </form>
    ''' % (nombreParametrosRecibirPost["Imagen"])
}

NOMBRE_ARCHIVO_RECIBIDO = "recibido.jpg"


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if nombreParametrosRecibirPost["Imagen"] not in request.files:
            return redirect(request.url)
        else:
            rutaImagen = request.files[nombreParametrosRecibirPost["Imagen"]]
            if rutaImagen.filename == '':
                return redirect(request.url)
            if rutaImagen and allowed_file(rutaImagen.filename):
                rutaImagen.save(NOMBRE_ARCHIVO_RECIBIDO)



                return "imagen recibida"
    return htmlRta["index"]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1990, debug=True)
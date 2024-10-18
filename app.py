from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal con menú de opciones
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para inscripción en curso
@app.route('/curso', methods=['GET', 'POST'])
def curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        curso = request.form['curso']
        return f'Inscripción exitosa: {nombre} en el curso {curso}'
    return render_template('curso.html')

# Ruta para registro de usuario
@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = request.form['password']
        return f'Usuario registrado: {nombre} {apellidos}, Email: {email}'
    return render_template('usuario.html')

# Ruta para registro de producto
@app.route('/producto', methods=['GET', 'POST'])
def producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        return f'Producto registrado: {nombre}, Categoría: {categoria}, Precio: {precio}'
    return render_template('producto.html')

# Ruta para registro de libro
@app.route('/libro', methods=['GET', 'POST'])
def libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        formato = request.form['formato']
        return f'Libro registrado: {titulo}, Autor: {autor}, Formato: {formato}'
    return render_template('libro.html')

if __name__ == '__main__':
    app.run(debug=True)

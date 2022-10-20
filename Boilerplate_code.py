#Importar el módulo Flask en el proyecto.
from operator import truediv
from flask import Flask, render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/index")

#‘/’ URL está vinculado con la función first_flask.
def first_flask():
    name = "Jhon"
    return render_template("index.html",index_variable = name)

#Ejecutamos la app en el servidor local.
app.run(debug=True)

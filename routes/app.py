from flask import Flask, render_template, request

app = Flask(__name__)

# Problema: al parecer los templates no se llegan a "conectar" con este
# código y además, en los html no se reconoce lo que va en {% %} lo imprime
# tal cual en la pantalla tipo sale -> {% extend "layout.html" %} en lugar
# de aplicar la parte de head que quise implementar desde ese template
# no me comuniqué con usted debido a que en los ejemplos de la clase me 
# ha ido todo bien y lo último que hice fue el .py y ahí me dí cuenta de los errores.
# Dejé los html sin los {% %} para que se siga viendo bien. 

@app.template("/") # iniciar el template Registro.html
def template():
    return render_template("Registro.html")

@app.route("/usuario", methods='POST') # obtener todos los datos para mandarlos a datos.html
def usuario():
    name = request.form("nombre")
    surname = request.form("apellido")
    date_bth = request.form("fecha_nac")
    email = request.form("email")
    
    return render_template("datos.html")

if __name__ == "__main__": # correr la aplicación en modo debug
    app.run(debug=True)
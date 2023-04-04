from flask import Flask  
app = Flask(__name__)   

@app.route('/')         
def hola_mundo():
    return 'Hola Mundo!'  

@app.route('/dojo')         
def dojo():
    return 'Dojo!'
#Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# acá puede decir el nombre de flask, Michael y John
@app.route('/say/<nombre>')
def saludo(nombre):
    return f'Hola {nombre}'

#Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):
#localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
@app.route('/repeat/35/<texto>')
def repeat(texto):
    texto = 'Hello' * 35
    return texto
#localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
@app.route('/repeat2/80/<adios>')
def repeat2(adios):
    adios = "bye" * 80
    return adios
#localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces

@app.route('/repeat3/99/<perrito>')
def repeat3(perrito):
    perrito = "dogs" * 99
    return 'perrito'
#BONUS NINJA: Para la cuarta tarea, asegúrate de que el segundo elemento en la URL sea un número entero y el tercer elemento sea una cadena
@app.route('/repeat4/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output
#BONUS SENSEI: Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
@app.errorhandler(404)
def error(e):    
    return 'Esta ruta no exite'

if __name__=="__main__":
    app.run(debug=True)      







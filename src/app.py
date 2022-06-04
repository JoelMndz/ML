from os import environ
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
#Cargar modelo predictivo
modelo = pickle.load(open('./src/EncuestaLR.model','rb'))


@app.route("/",methods=['GET'])
def hello_world():
  return render_template('formulario.html',data = {})

@app.route("/precedir", methods=['POST'])
def precedir():
  prediccion = modelo.predict([[
    int(request.form['pregunta1']),
    int(request.form['pregunta2']), 
    int(request.form['pregunta3']),
    int(request.form['pregunta4']),
    int(request.form['pregunta5'])]])
  data = {}
  if prediccion[0] == 0:
    data['mensaje'] = 'No es propenso a caer en la drogadicción 😊'
    data['color'] = 'success'
  else:
    data['mensaje'] = 'Tenga cuidado puede caer en la drogadicción 😥'
    data['color'] = 'danger'
  return render_template('formulario.html',data = data)

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000)
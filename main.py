from flask import Flask

#creem l'objecte de la classe importada, classe importada = Flask
app = Flask('__name__')

#route= part del URL
@app.route('/')
def hello_world():
  return 'hello, world'

#if serveix per inicialitzar l'objecte app i obrir la pagina web
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask,jsonify 
from googletrans import Translator
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
    return 'Hello World'


@app.route('/translate/<string:name>', methods=['GET'])
def translete_word(name):
    translator = Translator()
    initial_langu=translator.detect(name)
    result = translator.translate(name,dest='en')
    result2=translator.translate(name,dest=initial_langu)
    print(result.text)
    return jsonify({'data' : result.text})

  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True)

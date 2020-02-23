# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask,jsonify 
from googletrans import Translator
import requests  
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
    value=translator.detect(name)
    
    result = translator.translate(name,dest='en')
    result2=translator.translate(name,dest=value.lang)
    # print(result.text)
    return jsonify({'eng' : result.text,'orilan':result2.text,'lang':value.lang})


@app.route('/translate2/<name>/<name2>', methods=['GET'])
def translete_word2(name,name2):
    translator = Translator()
#     # value=translator.detect(name)
#     # # print(type(value))
#     # if value!='en':
#     #     result = translator.translate(name,dest=value.lang)
#     # else:
#     #     result = translator.translate(name,dest='en')    
#     # print(result.text)
#     # print("*************************")
#     # return {'data' : result.text}
#     # value=str(translator.detect(name))
#     # print(value)
    result = translator.translate(name2,dest=name)
#     #result2=translator.translate(name,dest=value.lang)
#     # print(result.text)
    return jsonify({'data' : result.text})




@app.route('/sentiment/<string:name1>', methods=['GET'])
def sentiment_sentence(name1):
    #translator = Translator()
    #result = translator.translate(name,dest='en')
    result = requests.post("https://api.deepai.org/api/sentiment-analysis",data={
        "text": name1,
    },
    headers = {"Api-Key":"quickstart-QUdJIGlzIGNvbWluZy4uLi4K"})
    return result.json()
    #return jsonify({'languages' : result.text})

@app.route('/know/<string:name2>')
def knowledgebases(name2):
    url = "https://api.mypurecloud.com/api/v2/knowledge/knowledgebases/c9b505b6-b7d1-4d42-8f8e-7fda131a2feb/search"

    payload = "{\n  \"query\": \""+name2+"\",\n  \"pageSize\": 1,\n  \"pageNumber\": 1,\n  \"languageCode\":\"en-US\",\n  \"documentType\": \"Faq\",\n  \"searchOnDraftDocuments\": \"True\"\n}"
    headers = {
    'organizationId': '9369c50e-6536-4ddc-b716-85122422d9fc',
    'Content-Type': 'application/json',
    'Authorization': 'bearer RMUwRadt7QeNUYZstzKY3SfOb4C84R_OIOB93MEEmdDxyHN5dYZEMogMh3wTcVulMTCdiEtSlJEHFMX4Y537nA'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    return response.json()
  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True, port=8080)# Importing flask module in the project is mandatory 

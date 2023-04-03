from flask import Flask
from flask import request, jsonify
import base_chat
app = Flask(__name__)

@app.route('/continue', methods=['GET'])
def promptNext():
    
    response = base_chat.on_message("+")
    output_string = response
    
    return output_string

@app.route('/api', methods=['GET'])
def prompt():

    text = request.args.get('prompt')
    
    response = base_chat.on_message(text)
    output_string = response
    
    return output_string

@app.route('/instruct', methods=['GET'])
def instruct():
    
    text = request.args.get('prompt')
    
    response = base_chat.on_message("+i " + text)
    output_string = response
    
    return output_string

@app.route('/reset', methods=['GET'])
def reset():
    base_chat.on_message("+reset")
    return "reset"

if __name__ == '__main__':
    app.run(debug=True)
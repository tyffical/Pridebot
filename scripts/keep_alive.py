# keeping bot alive on repl.it https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz

from flask import Flask, request
from threading import Thread
import json

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

@app.route('/refresh', methods = ['POST'])
def refresh():
    print(f"repl.deploy{json.loads(request.get_data())}{request.headers.get('Signature')}")
    deploy = input()
    print("repl.deploy-success")
    return json.loads(deploy)

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
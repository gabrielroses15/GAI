import time

from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/pergunta', methods=['GET'])
def consulta():
    prompt = request.get_json()
    import brain
    resposta = brain.brain(prompt=prompt)
    return jsonify(resposta)

app.run(port=5000, host="localhost", debug=True)
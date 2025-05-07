# app.py
from flask import Flask, request, jsonify
from fila_livros import adicionar_livro, retirar_livro

app = Flask(__name__)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    dados = request.json
    mensagem = adicionar_livro(dados['titulo'], dados['autor'])
    return jsonify({"mensagem": mensagem})

@app.route('/retirar', methods=['GET'])
def retirar():
    livro = retirar_livro()
    return jsonify(livro)

if __name__ == '__main__':
    app.run(port=5000)

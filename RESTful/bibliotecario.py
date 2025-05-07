# bibliotecario.py
import requests

titulo = input("Título do livro: ")
autor = input("Autor do livro: ")

resposta = requests.post("http://localhost:5000/adicionar", json={"titulo": titulo, "autor": autor})
print(f"[Bibliotecário] {resposta.json()['mensagem']}")

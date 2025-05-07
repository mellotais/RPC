# usuario.py
import requests

resposta = requests.get("http://localhost:5000/retirar")
livro = resposta.json()
print(f"[Usuário] Livro retirado: '{livro['titulo']}' por {livro['autor']}")

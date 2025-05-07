from zeep import Client

client = Client('http://localhost:8000/?wsdl')

resposta = client.service.PegarLivro()
titulo, autor = resposta.split("|")
print(f"[Usuário] Livro retirado: '{titulo}' por {autor}")
